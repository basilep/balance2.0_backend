from dataclasses import field
from glob import escape
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
import requests
from . models import *
from decode_alarme import decode_alarme_from_decimal
import asyncio
import websockets

# Create your views here.

# GLOBAL VAR
actual_msg_page = None
web_socket_client = None

# VIEWS

def index(request):  #Need request argument
    return render(request, '404.html')

# Manage alerts
@csrf_exempt
def alerts(request):
    if request.method == "POST":
        decimal_data = request.POST.get("alarme_data")
        alerts = decode_alarme_from_decimal(decimal_data)   # list of alerts
        for alert in alerts:
            try:
                Alert.objects.create(type=alert)
            except:
                pass 
    alerts = list(Alert.objects.values('id', 'type', 'created_at'))
    for alert in alerts:
        # Add the display name to each alert dictionary
        alert_obj = Alert.objects.get(id=alert['id'])
        alert['alert_name'] = alert_obj.get_type_display()
    return JsonResponse(alerts, safe = False)

# Manage temp and humidity
@csrf_exempt
def box_data(request):
    if request.method == "POST":
        temperature = request.POST.get("temperature")
        humidity = request.POST.get("humidity")
        try:
            BoxData.objects.create(temperature=temperature, humidity=humidity)
        except:
            pass
    return JsonResponse(list(BoxData.objects.values()), safe = False)

@csrf_exempt
def update_beer_data(request):
    if request.method == "POST":
        str_beer_1 = request.POST.get("str_beer_1")
        str_beer_2 = request.POST.get("str_beer_2")

        balance_1 = Balance.objects.get(id=1)
        balance_1.remaining_beer = str_beer_1
        balance_1.save()
        balance_2 = Balance.objects.get(id=2)
        balance_2.remaining_beer = str_beer_2
        balance_2.save()

        return JsonResponse(list(Balance.objects.values()), safe = False)
    

@csrf_exempt
def beers_on_balance(request):
    # Représente les données des bières sur les balances
    # TODO est-ce qu'on doit envoyer que celles actives?
    try:
        beer_1 = Balance.objects.get(id=1).related_beer
        beer_2 = Balance.objects.get(id=2).related_beer

        # Prepare the response data for both balances
        data = {
            "balance_1": {
                "name": beer_1.name,
                "weight_empty": beer_1.weight_empty,
                "rho": beer_1.rho,
                "quantity": beer_1.quantity
            },
           "balance_2": {
                "name": beer_2.name,
                "weight_empty": beer_2.weight_empty,
                "rho": beer_2.rho,
                "quantity": beer_2.quantity
            },
        }

        # Return the response as JSON
        return JsonResponse(data, status=200)
    except Balance.DoesNotExist:
        return JsonResponse({"error": "One or both balances do not exist."}, status=404)

#@login_required
@csrf_exempt
def beers(request):
    if request.method == "POST":    #If it's a POST request
        beers = Beer.objects.all()
        print(request.POST)
        #Check that the beer does not exist
        for beer in beers:
            if beer.name == request.POST.get("beer_name"):
                #If the beer exists, edit it
                beer_to_edit = Beer.objects.get(name = request.POST.get("beer_name"))
                beer_to_edit.name = request.POST.get("beer_name")
                beer_to_edit.weight_empty = request.POST.get("weight_empty")
                beer_to_edit.rho = request.POST.get("rho")
                beer_to_edit.quantity = request.POST.get("quantity")
                beer_to_edit.save()
                return JsonResponse(list(Beer.objects.values()), safe = False)
        #else, create it
        beer_name = request.POST.get("beer_name")
        weight_empty = request.POST.get("weight_empty")
        rho = request.POST.get("rho")
        quantity = request.POST.get("quantity")
        try:
            Beer.objects.create(name = beer_name, weight_empty= weight_empty, rho=rho, quantity=quantity)
        except:
            pass
    return JsonResponse(list(Beer.objects.values()), safe = False)

@csrf_exempt
def beer_json(request, beer_id):
    if(request.method == "DELETE"):    #If it's a DELETE request
        # Récupérez l'objet à supprimer
        obj = get_object_or_404(Beer, pk=beer_id)
        # Supprimez l'objet
        obj.delete()
        return JsonResponse(list(Beer.objects.values()), safe = False)
    else:
        data = json.loads(serializers.serialize("json", Beer.objects.filter(pk=beer_id))[1:-1])
        return JsonResponse(data["fields"])

@csrf_exempt
def balance(request,balance_id):
    if request.method == "POST":
        balance = Balance.objects.get(id = balance_id)
        # modifie les données de la balance
        if request.POST.get("related_beer_id"):
            balance.related_beer = Beer.objects.get(id=request.POST.get("related_beer_id")) #Change the current beer
            # notify the script
            beer_to_change = balance.related_beer
            data = {"balance_"+str(balance_id):{"name": beer_to_change.name,"weight_empty": beer_to_change.weight_empty,"rho": beer_to_change.rho,"quantity": beer_to_change.quantity}}
            asyncio.run(send_data_to_client(data))
        if request.POST.get("remaining_beer"):
            balance.remaining_beer = request.POST.get("remaining_beer")
        if request.POST.get("nomComplet"):
            balance.nomComplet = request.POST.get("nomComplet")
        if request.POST.get("nomSimple"):
            balance.nomSimple = request.POST.get("nomSimple")
        if request.POST.get("nameBeerOrCollective")!= None:
            balance.nameBeerOrCollective = request.POST.get("nameBeerOrCollective")
        if request.POST.get("activated")!= None:
            balance.activated = request.POST.get("activated")
        balance.save()
        #send changes to the script
        data = {"balance_"+str(balance_id):{"enable": balance.activated, "name": balance.nomSimple, "name_beer": balance.related_beer.name, "name_or_collectif": balance.nameBeerOrCollective}}
        asyncio.run(send_data_to_client(data))
    data = json.loads(serializers.serialize("json", Balance.objects.filter(pk=balance_id))[1:-1])
    tmp_data = data["fields"]
    tmp_data["id"] = balance_id

    return JsonResponse(tmp_data)

@csrf_exempt
def balances(request):
    return JsonResponse(list(Balance.objects.values()), safe = False)    

@csrf_exempt
def matrice_led(request):
    try:
        balance_1 = Balance.objects.get(id=1)
        balance_1_enable = balance_1.activated
        name_1 = balance_1.nomSimple
        name_beer_1 = balance_1.related_beer.name # Access related beer name directly through the foreign key
        name_or_collectif_1 = balance_1.nameBeerOrCollective

        balance_2 = Balance.objects.get(id=2)
        balance_2_enable = balance_2.activated
        name_2 = balance_2.nomSimple
        name_beer_2 = balance_2.related_beer.name
        name_or_collectif_2 = balance_2.nameBeerOrCollective

        data = {
                "balance_1": {
                    "enable": balance_1_enable,
                    "name": name_1,
                    "name_beer": name_beer_1,
                    "name_or_collectif": name_or_collectif_1,
                },
                "balance_2": {
                    "enable": balance_2_enable,
                    "name": name_2,
                    "name_beer": name_beer_2,
                    "name_or_collectif": name_or_collectif_2,
                }
            }
        
        return JsonResponse(data, status=200)
    except Balance.DoesNotExist:
        return JsonResponse({"error": "One or both balances do not exist."}, status=404)

# Synchronous view to handle POST request
@csrf_exempt
def manage_data_to_script(request):
    if request.method == "POST":
        
        received_data = json.loads(request.body)  # Parse the JSON body
        keys = received_data.keys()   # Should have only one key
        key = [key for key in keys]

        if len(key) > 1:
            return JsonResponse({'status': 'error', 'message': 'Invalid usage of the method'}, status=500)
        
        elif key[0] == "message":
            received_data = json.loads(request.body)  # Parse JSON body
            message_data = received_data.get("message")
            permanent = message_data.get("permanent")
            freq = message_data.get("freq")
            msg = message_data.get("message")
            scroll = message_data.get("scroll")
            actual_msg_page = {"message": msg, "freq":freq, "permanent":permanent, "scroll":scroll}

        #elif key[0] == "matrice_led":
        # Trigger WebSocket data sending (runs async code in a synchronous view)

        asyncio.run(send_data_to_client(actual_msg_page))
        
        return JsonResponse({'status': 'success', 'message': 'Data received and processed successfully.'}, status=200)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


async def websocket_handler(websocket, path):
    global connected_client
    connected_client = websocket  # Store the connected client
    try:
        # Keep the connection open indefinitely
        await asyncio.Future()  # Keep connection open until client disconnects
    finally:
        connected_client = None  # Reset when the client disconnects

# Function to send data to the single client
async def send_data_to_client(data):
    global connected_client
    if connected_client:  # Only send if there is a connected client
        data = json.dumps(data) # Covert json to string
        await connected_client.send(data)
        print(f"Sent data to the client: {data}")
    else:
        print("No client connected.")

def start_web_socket_server():
    print("Je run le server, normalement ça va fonctionner")
    asyncio.run(run_websocket_server())

# WebSocket server starter
async def run_websocket_server():
    async with websockets.serve(websocket_handler, "localhost", 5000):
        await asyncio.Future()  # Keep the server running


def affond(request):
    return render(request, '404.html')

@csrf_exempt
def login_user(request):
    print(request.COOKIES)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("success")
            login(request, user)
        else:
            print("error")
    #Need to have a login html (in templates)
    return render(request, '404.html')
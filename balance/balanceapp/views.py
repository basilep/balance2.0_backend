from dataclasses import field
from glob import escape
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
import requests
from . models import *


# Create your views here.

# GLOBAL VAR
actual_msg_page = None

# VIEWS

def index(request):  #Need request argument
    return render(request, '404.html')

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

def beer_json(request, beer_id):
    data = json.loads(serializers.serialize("json", Beer.objects.filter(pk=beer_id))[1:-1])
    return JsonResponse(data["fields"])

@csrf_exempt
def beers_remove(request):
    beers = Beer.objects.all()
    if request.method == "POST":
        for beer in beers:
            if beer.name == request.POST.get("beer_name"):
                beer_to_remove = Beer.objects.get(name = request.POST.get("beer_name"))
                beer_to_remove.delete() #Remove the beer from the db
                return render(request, '404.html')
    return render(request, '404.html')

@csrf_exempt
def balance(request,balance_id):
    if request.method == "POST":
        if request.POST.get("remaining_beer") != None:
            # modifie la quantité des bières (Depuis la balance)    
            balance = Balance.objects.get(id = balance_id)
            balance.remaining_beer = request.POST.get("remaining_beer")
            balance.save()
        elif request.POST.get("activated")!= None:
            balance = Balance.objects.get(id = balance_id)
            print(request.POST.get("activated"))
            balance.activated = request.POST.get("activated")
            balance.save()
        elif request.POST.get("sentence_display")!= None:
            balance = Balance.objects.get(id = balance_id)
            print(request.POST.get("sentence_display"))
            balance.sentence_display = request.POST.get("sentence_display")
            balance.save()
    data = json.loads(serializers.serialize("json", Balance.objects.filter(pk=balance_id))[1:-1])
    tmp_data = data["fields"]
    # Get the beer name
    beer = Beer.objects.get(id = int(tmp_data["related_beer"]))
    tmp_data["related_beer"] = beer.name
    return JsonResponse(tmp_data)

#@login_required
@csrf_exempt
def message_to_script(request):
    global actual_msg_page  #To use the global variable
    if actual_msg_page == None:
        actual_msg_page = ""
        # Pas encore de message
    if request.method == "POST":
        permanent = request.POST.get("permanent")
        freq = request.POST.get("freq")
        msg = request.POST.get("message")
        scroll = request.POST.get("scroll")
        actual_msg_page = {"message": msg, "freq":freq, "permanent":permanent, "scroll":scroll}
        ########################
        ##    WEBHOOK PART    ##
        ########################
        try:
            requests.post('http://127.0.0.1:5000/webhook', data=json.dumps(actual_msg_page), headers={'Content-Type':'application/json'})
        except:
            print("The server is not reachable") 
    #print(actual_msg_page)
    return JsonResponse(actual_msg_page, safe = False)
"""
@csrf_exempt
@login_required
def message(request):
    msgs = Message.objects.all()
    if request.method == "POST":
        for msg in msgs:
            if msg.message == request.POST.get("msg"):
                print("Existe déjà")
                return render(request, 'beers.html', {'messages':msgs})
        permanent = request.POST.get("permanent")
        freq = request.POST.get("freq")
        
        msg = request.POST.get("msg")
        #freq and permanent send to the raspberry
        Message.objects.create(message=msg)
        msgs = Message.objects.all()
    return render(request, 'message.html', {'messages':msgs})"""

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
from dataclasses import field
from glob import escape
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from . models import *


# Create your views here.

# GLOBAL VAR
actual_msg_page = None

# VIEWS

def index(request):  #Need request argument
    example_data = ["souye", "xeu le deux", "yaaaaaa"]

    return render(request, 'index.html', {'example':example_data})

@csrf_exempt
@login_required
def beers(request):
    beers = Beer.objects.all()
    if request.method == "POST":    #If it's a POST request
        print(request.POST)
        #Check that the bier does not exist
        for beer in beers:
            if beer.name == request.POST.get("beer_name"):
                return render(request, '404.html')
        #data = request.POST
        beer_name = request.POST.get("beer_name")
        weight_empty = request.POST.get("weight_empty")
        rho = request.POST.get("rho")
        quantity = request.POST.get("quantity")
        try:
            Beer.objects.create(name = beer_name, weight_empty= weight_empty, rho=rho, quantity=quantity)

        except:
            pass
    return render(request, '404.html')


def beers_json(request):
    return JsonResponse(list(Beer.objects.values()), safe = False)

def beer_json(request, beer_id):
    data = json.loads(serializers.serialize("json", Beer.objects.filter(pk=beer_id))[1:-1])
    return JsonResponse(data["fields"])

@csrf_exempt
@login_required
def message_to_script(request):
    global actual_msg_page  #To use the global variable
    if actual_msg_page == None:
        actual_msg_page = ""
        print("souye")
    if request.method == "POST":
        permanent = request.POST.get("permanent")
        freq = request.POST.get("freq")
        msg = request.POST.get("message")
        actual_msg_page = {"message": msg, "freq":freq, "permanent":permanent}
    print(list(actual_msg_page), safe = False)
    return JsonResponse(list(actual_msg_page), safe = False)

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
    return render(request, 'message.html', {'messages':msgs})

def affond(request):
    return render(request, 'affond.html')

def test(request, test_id):
    return render(request, 'index.html', {'id': test_id})

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
    return render(request, 'login.html')
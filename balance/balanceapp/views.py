from django.shortcuts import render

from . models import *
# Create your views here.
def index(request):  #Need request argument
    example_data = ["souye", "xeu le deux", "yaaaaaa"]

    return render(request, 'index.html', {'example':example_data})

def beers(request):
    beers = Beer.objects.all()  #Get all beers
    return render(request, 'beers.html')

def test(request, test_id):
    return render(request, 'index.html', {'id': test_id})

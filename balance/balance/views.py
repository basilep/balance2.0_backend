from django.shortcuts import render
#from django.http import HttpResponse

def home(request):  #Need request argument
    return render(request, '404.html')
    
def handler404(request, exception):
    return render(request, "404.html", {"error":exception}, status=404)
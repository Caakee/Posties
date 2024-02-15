from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(response):
    return render(response, "main/home.html")

def v1(response):
    return HttpResponse("<h1>view 1</h1>")
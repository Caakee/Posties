from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(response):
    return render(response, "main/home.html")

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = UserCreationForm()
    
    return render(response, "register/register.html", {"form":form})
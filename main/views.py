from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import JsonResponse
from .models import Event
from django.utils.timezone import datetime

# Create your views here.
def home(response):
    all_events = Event.objects.all()
    context = {
        "events": all_events,
    }
    return render(response, "main/home.html")

def all_events(request):
    all_events = Event.objects.all()
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })

    return JsonResponse(out, safe=False)
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Event(name=str(title), start=start, end=end)
    event.username = request.user
    event.userID = request.user.id
    event.log_date = datetime.now()
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    
    return render(response, "register/register.html", {"form":form})
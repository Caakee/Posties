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
            'username': event.username,
        })

    return JsonResponse(out, safe=False)
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    username = request.GET.get("username", None)
    userID = request.user.id
    log_date = datetime.now()
    event = Event(name=str(title), start=start, end=end, username=str(username), userID=userID, log_date=log_date)
    event.save()
    data = {}
    return JsonResponse(data)

def edit(request):
    return JsonResponse(data)

def remove(request):
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    username = request.GET.get("username", None)
    if(username == event.username):
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
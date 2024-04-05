from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import JsonResponse
from .models import Event
from dateutil.parser import parse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UpdateProfileForm

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
            'log_date': event.log_date.strftime("%#m/%#d/%Y, %#I:%M:%S %p"), # The formatting prevents the date format from changing after a post edit
        })

    return JsonResponse(out, safe=False)
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    username = request.GET.get("username", None)
    log_date = parse(request.GET.get("log_date", None)) # Parse makes sure the date is of the right format, it cannot be passed otherwise
    event = Event(name=str(title), start=start, end=end, username=str(username), log_date=log_date)
    event.save()
    data = {}
    return JsonResponse(data)

def edit(request):
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    title = request.GET.get("title", None)
    username = request.GET.get("username", None)
    if (username == event.username):
        event.name = str(title)
        event.save()
    data = {}
    return JsonResponse(data)

def remove(request):
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    username = request.GET.get("username", None)
    if (username == event.username):
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

def help(response):
    return render(response, "main/help.html")

@login_required
def my_profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully')
            return redirect(to='my_profile')
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'main/my_profile.html', {'profile_form': profile_form})

def profile(request, username):
    return render(request, 'main/profile.html')
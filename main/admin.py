from django.contrib import admin
from .models import Event
from .models import Profile

# Register your models here.
admin.site.register(Event)
admin.site.register(Profile)
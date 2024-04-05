from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('<username>/', views.profile, name='user_profile'),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('profile/', views.my_profile, name='my_profile'),
    path('profile/<username>/', views.profile, name='user_profile'),
]
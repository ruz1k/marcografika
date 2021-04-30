from django.urls import path
from . import views

app_name = "about-us"
urlpatterns = [
    path('', views.aboutUs, name='aboutUs'),
]
from django.urls import path
from . import views

app_name = "mediabank"
urlpatterns = [
    path('', views.media_photo, name='media_photo'),
]
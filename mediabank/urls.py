from django.urls import re_path
from . import views

app_name = "mediabank"
urlpatterns = [
    re_path(r'^$', views.media_photo, name='media_photo'),
]
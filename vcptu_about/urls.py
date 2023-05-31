
from django.urls import path

from . import views

app_name = 'vcptu_about'

urlpatterns = [
    path('', views.aboutPage, name="aboutPage")
]

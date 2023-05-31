
from django.urls import path

from . import views

app_name = 'vcptu_home'

urlpatterns = [
    path('', views.homePage, name="homePage")
]

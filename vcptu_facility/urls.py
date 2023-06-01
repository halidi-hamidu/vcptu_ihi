
from django.urls import path

from . import views

app_name = 'vcptu_facility'

urlpatterns = [
    path('', views.facilityPage, name="facilityPage")
]

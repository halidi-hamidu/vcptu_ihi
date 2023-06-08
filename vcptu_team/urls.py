
from django.urls import path

from . import views

app_name = 'vcptu_team'

urlpatterns = [
    path('', views.teamPage, name="teamPage"),
    path('team-Detail/<str:id>/', views.teamDetailPage, name="teamDetailPage")
]



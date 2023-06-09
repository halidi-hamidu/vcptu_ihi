
from django.urls import path

from . import views

app_name = 'vcptu_news'

urlpatterns = [
    path('', views.newsPage, name="newsPage"),
    path('news-details/<str:id>/', views.newsDetailPage, name="newsDetailPage")
]

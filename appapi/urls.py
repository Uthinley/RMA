from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiover, name="apiover"),
    path('goldrates/', views.Goldlist, name="Goldlist"),
    path('goldratesDetail/<str:id>/', views.GoldlistDetail, name="GoldlistDetail"),
]
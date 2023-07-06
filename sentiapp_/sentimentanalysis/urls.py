from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', templates.index),
    path('', views.index, name="home"),
]
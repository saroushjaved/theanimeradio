from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.polling, name="polling"),
    path("pollingpage", views.polling_page, name="pollingpage")
]
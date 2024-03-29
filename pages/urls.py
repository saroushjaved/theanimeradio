"""theanimeradio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('list2018', views.list2018, name="list2018"),
    path('list2019', views.list2019, name="list2019"),
    path('summer2020', views.summer2020, name="summer2020"),
    path('winter2020', views.winter2020, name="winter2020"),
    path('spring2020', views.spring2020, name="spring2020"),
    path('sitemap', views.sitemap, name="sitemap"),
]

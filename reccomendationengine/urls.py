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
    path('', views.reccomendation_home, name="reccomendationhome"),
    path('engine', views.reccomendation_engine, name="reccomendationengine"),
    path('recc1', views.recc1, name="reccomendatio-question-1"),
    path('recc2', views.recc2, name="reccomendatio-question-2"),
    path('recc3', views.recc3, name="reccomendatio-question-3"),
    path('recc4', views.recc4, name="reccomendatio-question-4"),
    path('genre_before_2010', views.genre_before_2010, name="genre_before_2010"),
    path('genre_after_2010', views.genre_after_2010, name="genre_after_2010"),
    path('sliceoflife_after_2010', views.sliceoflife_after_2010, name="sliceoflife_after_2010"),
    path('sliceoflife_before_2010', views.sliceoflife_before_2010, name="sliceoflife_before_2010"),
    path('isekai_after_2010', views.isekai_after_2010, name="isekai_after_2010"),
    path('isekai_before_2010', views.isekai_before_2010, name="isekai_before_2010"),
    path('shonin_after_2010', views.shonin_after_2010, name="shonin_after_2010"),
    path('shonin_before_2010', views.shonin_before_2010, name="shonin_before_2010"),

]

from django.contrib import admin
from . models import RecommendationDatabase
# Register your models here.

class RecommendationDatabaseAdmin(admin.ModelAdmin): 
    list_display = ('name', 'imdb', 'image', "summary", "Year2010", "genre", "sub_genre", "crunchyroll", "info") 
  
  
admin.site.register(RecommendationDatabase)

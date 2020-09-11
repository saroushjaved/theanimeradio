from django.contrib import admin

# Register your models here.
from .models import Polls, Choices



admin.site.register(Polls)

admin.site.register(Choices)

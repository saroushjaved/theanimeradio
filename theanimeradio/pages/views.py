from django.shortcuts import render
from pages.models import List2018

# Create your views here.
def home(request):
    return render(request, 'index.html')

def list2018(request):
    
    list1 = List2018.objects.all().order_by("-up_votes")

    return render(request, 'list2018.html',{'list_2018':list1})

def signup(request):
    return render(request, 'signup.html')

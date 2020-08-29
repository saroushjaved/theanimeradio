from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
import requests
from django.contrib.auth import logout

# Create your views here.
def signup(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        username=request.POST['username']
        password2 = request.POST['password2']
        email = request.POST['email']

        if len(password1) >= 8: 
            if password1 != password2:
                messages.info(request, " Password must be 8 Character Long " )
                return redirect('/usersreg/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken" )
                return redirect('/usersreg/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username is already taken" )
                return redirect('/usersreg/signup')
            
            else:
                user = User.objects.create_user( username=username, first_name=first_name , last_name=last_name , password=password1)
                user.save()
                messages.info(request, "Registration Successful" )
                return redirect('/usersreg/signup')
        else:
            messages.info(request, " Password must be 8 Character Long " )
            return redirect('/usersreg/signup')
    
    else:
        return render(request, 'signup.html')

    
def login(request):

    if request.method == "POST":

        username=request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Login Done")
            return render(request, "login.html")
        else:
            messages.info(request, "Wrong Password or Username")
            return render(request, 'signup.html')
    
    else:
        return render(request, "signup.html")

def loginpage(request):
    if request.user.is_authenticated:
        return render(request, 'login.html')

    else:
        return redirect("/usersreg/signup")



def logout_module(request):
    logout(request)
    return render(request, 'index.html')
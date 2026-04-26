from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout

# Create your views here.
def signup(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        password1 = request.POST.get('password1', '')
        username = request.POST.get('username', '').strip()
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '').strip()

        if len(password1) >= 8: 
            if password1 != password2:
                messages.info(request, "Passwords do not match.")
                return redirect('/usersreg/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken" )
                return redirect('/usersreg/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken" )
                return redirect('/usersreg/signup')
            elif not username:
                messages.info(request, "Username is required.")
                return redirect('/usersreg/signup')
            
            else:
                user = User.objects.create_user( username=username, first_name=first_name , last_name=last_name , password=password1, email=email)
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

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Login Done")
            return render(request, "login.html")
        else:
            messages.info(request, "Wrong Password or Username")
            return redirect('/usersreg/signup')
    
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

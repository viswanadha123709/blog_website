from django.shortcuts import render, redirect
from .models import credentials
from django.contrib.auth import authenticate,login as authlogin

def register(request):
    if request.method == "POST":
        username = request.POST.get("new_username")
        password = request.POST.get("new_password")

        credentials.objects.create(
            name=username,
            password=password
        )

        

    return render(request, "register.html")

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            authlogin(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid Username or Password"})

    return render(request, "login.html")

def main(request):
    return render(request,"main.html")
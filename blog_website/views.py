from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

# Create your views here.
def login(request):
    if request.method=='POST':
        userid=request.POST.get("userid")
        password=request.POST.get("password")
        user=authenticate(request,username=userid,password=password)
        if user is not None:
            login(request, user)
            return redirect("home")


        

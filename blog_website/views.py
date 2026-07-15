from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        username = request.POST.get("new_username")
        password = request.POST.get("new_password")

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("login")

    return render(request, "first.html")
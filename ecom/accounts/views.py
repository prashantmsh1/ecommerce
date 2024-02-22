from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Create your views here.


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(username=email)
        print(user_obj)
        if user_obj.exists():
            print("user found")
        if not user_obj.exists():
            messages.error(request, "User not found.")
            return HttpResponseRedirect(request.path_info)

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "Email not verified.")
            return HttpResponseRedirect(request.path_info)
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return HttpResponseRedirect(request.path_info)

        else:
            messages.error(request, "Invalid credentials.")
            return HttpResponseRedirect(request.path_info)

    return render(request, "accounts/login.html")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            messages.error(request, "Already exists.")
            return HttpResponseRedirect(request.path_info)
        if password1 != password2:
            messages.error(request, "Password does not match.")
            return render(request, "accounts/register.html ")
        else:
            password = password1
            user_obj = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=email,
                email=email,
            )
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "An email has been sent to you.")
            return HttpResponseRedirect(request.path_info)
    return render(request, "accounts/register.html")


def activate_account(request, email_token):
    try:
        profile_obj = Profile.objects.get(email_token=email_token)
        profile_obj.is_email_verified = True
        profile_obj.save()
        messages.success(request, "Email verified.")
        return redirect("/accounts/login")
    except Exception as e:
        return HttpResponse("Invalid link")

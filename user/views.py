from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from requests import request
from . import forms
from django.contrib.auth import login,authenticate

# Create your views here.

def register(request):
    form = forms.RegisterForm()

    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request,user)
            print(form.errors)
            return redirect("user:login")
        print(form.errors)

    context = {
        "form" : form
    }
    return render(request,"register.html",context)
    

def login_view(request):
    form = forms.LoginForm
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)

        if user is None:
            print(user)
            raise ValidationError(request,"Xeta")
        else:
            login(request,user)
            return redirect("posts:home")
    context = {
        "form":form
    }
    return render(request,"login.html",context)
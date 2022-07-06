from django.shortcuts import redirect, render

from . import forms
from . import models
from django.db.models import Q, fields

# Create your views here.

def homepage(request):
    form = forms.PostForm

    posts = models.PostModel.objects.filter(user=request.user)
    
    if request.method == "POST":
        form = forms.PostForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save_m2m()
            return redirect("posts:home")

    context = {
        "form" : form,
        "posts" : posts,
    }
    return render(request,"home.html",context)


def search(request):
    query = request.GET["q"]
    search_results = models.PostModel.objects.filter(
        Q(title__icontains=query,user=request.user) | Q(description__icontains=query,user=request.user)
    )

    context = {
        "search_results" : search_results
    }
    return render(request,"search.html",context)


def delete_post(request,id):
    post = models.PostModel.objects.get(id=id)
    post.delete()
    return redirect("posts:home")


def update_post(request,id):
    post = models.PostModel.objects.get(id=id)
    form = forms.PostForm(instance=post)
    if request.method == "POST":
        form = forms.PostForm(request.POST,request.FILES ,instance = post)
        print(form.errors)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save_m2m()
            return redirect("posts:home")
            
    context = {
        "form": form
    }
    return render(request,"update.html",context)

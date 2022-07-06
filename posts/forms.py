from django import forms
from . import models

class PostForm(forms.ModelForm):


    class Meta:
        model = models.PostModel
        fields = ["title","description","image","tags"]
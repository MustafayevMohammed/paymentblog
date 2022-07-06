from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

# Create your models here.


class PostModel(models.Model):
    user = models.ForeignKey(User,related_name="user_posts",on_delete=models.CASCADE)
    title = models.CharField(max_length=300,null=True,blank=False)
    description = RichTextField(null=False,blank=False)
    image = models.ImageField(null=False,blank=False,default="/1386843.png",upload_to="media/")
    tags = TaggableManager()

    def __str__(self):
        return self.title


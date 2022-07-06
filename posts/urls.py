from django.urls import path
from . import views
app_name = "posts"

urlpatterns = [
    path("home",views.homepage, name="home"),
    path("search",views.search, name="search"),
    path("delete/<int:id>",views.delete_post, name="delete"),
    path("update/<int:id>",views.update_post, name="update"),
]

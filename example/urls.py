from django.urls import path
from example import views

urlpatterns = [
    path("", views.home, name="home"),
    path("example/<name>", views.hello_there, name="hello_there"),
]
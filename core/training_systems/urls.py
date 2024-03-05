from django.urls import path
from training_systems import views

urlpatterns = [
    path("", views.course, name="home"),
    path("lessons/", views.lessons, name="lessons"),
    path("group/", views.group, name="group"),
]
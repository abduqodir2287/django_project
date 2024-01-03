from django.urls import path
from . import views

urlpatterns = [
    path("very_first/", views.members, name="members"),
    path("goat/", views.goat, name="goat"),
    path("best/", views.best_players, name="best"),
    path("first/", views.first, name="first"),
    path("", views.welcome, name="welcome"),
    path("second/", views.second, name="second"),
    path("the_best/", views.footballers, name="the_best"),
    path("users/", views.temp, name="temp"),
    path("teachers/", views.teachers, name="teachers"),
    path("help/", views.all_commands, name="help"),
    path("login/", views.login, name="login"),
    path("testing/", views.testing, name="testing")
]


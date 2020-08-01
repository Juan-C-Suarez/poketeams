from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("build", views.teambuilder, name="teambuilder"),
    path("teams", views.teams, name="teams"),
    path("like", views.like, name="like"),
    path("team/<int:id>", views.team, name="team"),
    path("stats", views.stats, name="stats"),
    path("pokemon/<int:number>", views.pokemon, name="pokemon")
]
from django.contrib.auth import authenticate, login, logout
#from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
#import json
from .models import User, Pokemon, Team, Team_member, Comment


def index(request):
    return render(request, "teambuilder/index.html")


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "teambuilder/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "teambuilder/login.html")


def register(request): #use a Django form in order to validate fields
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        fav_pkmn = get_pokemon(request.POST["fav_pkmn"])

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "teambuilder/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.favorite_pokemon = fav_pkmn
            user.save()
        except IntegrityError:
            return render(request, "teambuilder/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "teambuilder/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def profile(request, username):
    try:
        user = User.objects.get(username=username)
        return render(request, "teambuilder/profile.html", {
            "user": user
        })
    except User.DoesNotExist:
        return render(request, "teambuilder/error.html", {
            "message": "User not found"
        })


def teambuilder(request):
    if request.user.is_authenticated:
        return render(request, "teambuilder/teambuilder.html")
    else:
        return HttpResponseRedirect(reverse("index"))


def get_pokemon(number):
    try:
        pokemon = Pokemon.objects.get(number=number)
    except Pokemon.DoesNotExist:
        pokemon = Pokemon(number=number)
        pokemon.save()
    return pokemon

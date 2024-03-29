from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django import forms
from .models import User, Pokemon, Team, Team_member
from django.db.models import Count
import json


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
        points = Team.objects.filter(user=user).aggregate(total_points=Count('points'))
        print(points)
        return render(request, "teambuilder/profile.html", {
            "profile_user": user,
            "points": points["total_points"]
        })
    except User.DoesNotExist:
        return render(request, "teambuilder/error.html", {
            "message": "User not found"
        })


def teambuilder(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = User.objects.get(username=request.user.username)
            team = Team(user=user, name=request.POST["team-name"], strategy=request.POST.get("strategy", ""))
            team.save()
            pokemon1 = get_pokemon(request.POST["species1"])
            pokemon2 = get_pokemon(request.POST["species2"])
            pokemon3 = get_pokemon(request.POST["species3"])
            pokemon4 = get_pokemon(request.POST["species4"])
            pokemon5 = get_pokemon(request.POST["species5"])
            pokemon6 = get_pokemon(request.POST["species6"])
            team_member1 = Team_member(team=team, pokemon=pokemon1, ability=request.POST["ability1"], held_item=request.POST["item1"], nature=request.POST["nature1"], move1=request.POST["move1-1"], move2=request.POST["move1-2"], move3=request.POST["move1-3"], move4=request.POST["move1-4"])
            team_member1.save()
            team_member2 = Team_member(team=team, pokemon=pokemon2, ability=request.POST["ability2"], held_item=request.POST["item2"], nature=request.POST["nature2"], move1=request.POST["move2-1"], move2=request.POST["move2-2"], move3=request.POST["move2-3"], move4=request.POST["move2-4"])
            team_member2.save()
            team_member3 = Team_member(team=team, pokemon=pokemon3, ability=request.POST["ability3"], held_item=request.POST["item3"], nature=request.POST["nature3"], move1=request.POST["move3-1"], move2=request.POST["move3-2"], move3=request.POST["move3-3"], move4=request.POST["move3-4"])
            team_member3.save()
            team_member4 = Team_member(team=team, pokemon=pokemon4, ability=request.POST["ability4"], held_item=request.POST["item4"], nature=request.POST["nature4"], move1=request.POST["move4-1"], move2=request.POST["move4-2"], move3=request.POST["move4-3"], move4=request.POST["move4-4"])
            team_member4.save()
            team_member5 = Team_member(team=team, pokemon=pokemon5, ability=request.POST["ability5"], held_item=request.POST["item5"], nature=request.POST["nature5"], move1=request.POST["move5-1"], move2=request.POST["move5-2"], move3=request.POST["move5-3"], move4=request.POST["move5-4"])
            team_member5.save()
            team_member6 = Team_member(team=team, pokemon=pokemon6, ability=request.POST["ability6"], held_item=request.POST["item6"], nature=request.POST["nature6"], move1=request.POST["move6-1"], move2=request.POST["move6-2"], move3=request.POST["move6-3"], move4=request.POST["move6-4"])
            team_member6.save()
            return HttpResponseRedirect(reverse("profile", kwargs={"username": request.user.username}))

        else:
            return render(request, "teambuilder/teambuilder.html")
    else:
        return HttpResponseRedirect(reverse("index"))


def teams(request):
    order = request.GET["order"]
    start = int(request.GET["start"])
    end = int(request.GET["end"])
    
    if order == "most-popular":
        orderedTeams = Team.objects.annotate(count=Count('points')).order_by('-count')
    elif order == "newest":
        orderedTeams = Team.objects.order_by('-timestamp')
    else:
        orderedTeams = Team.objects.order_by('timestamp')

    if request.GET.get("user"):
        orderedTeams = orderedTeams.filter(user=User.objects.get(id=request.GET["user"]))
    if request.GET.get("pokemon"):
        orderedTeams = orderedTeams.filter(members=Pokemon.objects.get(number=request.GET["pokemon"]))

    teams = []

    if orderedTeams.count() < end:
        end = orderedTeams.count()


    for i in range(start, end):
        teams.append(orderedTeams[i])

    teams_data = []
    for team in teams:
        pokemon = []
        username = team.user.username
        #An attribute that tells if the user has liked this team
        if team.points.filter(username = request.user.username):
            liked = True
        else:
            liked = False
        #An attribute that tells the username of the user that created the team
        team_members = team.members.all()
        for pkmn in team_members:
            pokemon.append(pkmn.number)
        team_data = {
            "id": team.id,
            "name": team.name,
            "points": team.points.count(),
            "members": pokemon,
            "liked": liked,
            "username": username
        }
        teams_data.append(team_data)

    return JsonResponse({
        "teams": teams_data
    })


def like(request):
    if request.method == 'PUT':
        user = User.objects.get(username=request.user.get_username())
        data = json.loads(request.body)
        team_id = data.get("team_id")
        team = Team.objects.get(id=team_id)
        if data.get("like"):
            user.liked_posts.add(team)
        else:
            user.liked_posts.remove(team)
        user.save()
        return HttpResponse(status=204)


def team(request, id):
    team = Team.objects.get(id = id)
    if team is None:
        return render(request, "teambuilder/error.html", {
            "message": "Team not found."
        })
    else:
        pokemon = []
        username = team.user.username
        #An attribute that tells if the user has liked this team
        if team.points.filter(username = request.user.username):
            liked = True
        else:
            liked = False
        #An attribute that tells the username of the user that created the team
        team_members = Team_member.objects.filter(team=team)
        for pkmn in team_members:
            pokemon.append({
                "number": pkmn.pokemon.number,
                "ability": pkmn.ability.capitalize(),
                "held_item": pkmn.held_item.capitalize(),
                "nature": pkmn.nature.capitalize(),
                "move1": pkmn.move1.capitalize(),
                "move2": pkmn.move2.capitalize(),
                "move3": pkmn.move3.capitalize(),
                "move4": pkmn.move4.capitalize()
            })
        team_data = {
            "id": team.id,
            "name": team.name,
            "points": team.points.count(),
            "strategy": team.strategy,
            "members": pokemon,
            "liked": liked,
            "username": username
        }
        return render(request, "teambuilder/team.html", {
            "team_data": team_data
        })


def stats(request):
    pokemon = []
    orderedPokemon = Pokemon.objects.annotate(team_count=Count('teams')).filter(team_count__gt = 0).order_by('-team_count')[:10]
    for pkmn in orderedPokemon:
        pokemon.append({
            "number": pkmn.number,
            "count": pkmn.team_count
        })
    return render(request, "teambuilder/stats.html", {
            "pokemon": pokemon
        })


def pokemon(request, number):
    if number in range(1, 807):
        return render(request, "teambuilder/pokemon.html", {
            "number": number
        })
    else:
        return render(request, "teambuilder/error.html", {
            "message": "Pokemon not found."
        })


def get_pokemon(number):
    try:
        pokemon = Pokemon.objects.get(number=number)
    except Pokemon.DoesNotExist:
        pokemon = Pokemon(number=number)
        pokemon.save()
    return pokemon


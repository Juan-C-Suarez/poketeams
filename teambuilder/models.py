from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime   

class Pokemon(models.Model):
    number = models.IntegerField(validators=[MaxValueValidator(807), MinValueValidator(1)])

class User(AbstractUser):
    favorite_pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True)
    models.IntegerField(validators=[MaxValueValidator(892), MinValueValidator(1)])

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    private = models.BooleanField(default=False)
    points = models.ManyToManyField(User, related_name="liked_posts")
    name = models.CharField(max_length=50)
    strategy = models.CharField(max_length=1000)
    members = models.ManyToManyField(Pokemon, through='Team_member', related_name="teams")

class Team_member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    ability = models.CharField(max_length=50)
    held_item = models.CharField(max_length=50)
    nature = models.CharField(max_length=50)
    move1 = models.CharField(max_length=50)
    move2 = models.CharField(max_length=50)
    move3 = models.CharField(max_length=50)
    move4 = models.CharField(max_length=50)
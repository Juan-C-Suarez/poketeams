from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime   

class User(AbstractUser):
    favorite_pokemon = models.IntegerField(validators=[MaxValueValidator(892), MinValueValidator(1)])

class Pokemon(models.Model):
    number = models.IntegerField(validators=[MaxValueValidator(807), MinValueValidator(1)])

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
    ability = models.IntegerField(validators=[MaxValueValidator(293), MinValueValidator(1)])
    held_item = models.IntegerField(validators=[MaxValueValidator(1018), MinValueValidator(1)]) #Berries from 1 to 64, items form 65 to 1018
    nature = models.IntegerField(validators=[MaxValueValidator(25), MinValueValidator(1)])
    move1 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    move2 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    move3 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    move4 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="comments")
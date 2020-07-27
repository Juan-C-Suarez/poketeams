from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    favorite_pokemon = models.IntegerField(validators=[MaxValueValidator(892), MinValueValidator(1)])

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)
    points = models.ManyToManyField(User, related_name="liked_posts")
    name = models.CharField(max_length=50)
    strategy = models.CharField(max_length=1000)

    pkmn1_number = models.IntegerField(validators=[MaxValueValidator(807), MinValueValidator(1)])
    pkmn1_ability = models.IntegerField(validators=[MaxValueValidator(293), MinValueValidator(1)])
    pkmn1_held_item = models.IntegerField(validators=[MaxValueValidator(1018), MinValueValidator(1)]) #Berries from 1 to 64, items form 65 to 1018
    pkmn1_nature = models.IntegerField(validators=[MaxValueValidator(25), MinValueValidator(1)])
    pkmn1_move1 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn1_move2 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn1_move3 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn1_move4 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])

    pkmn2_number = models.IntegerField(validators=[MaxValueValidator(807), MinValueValidator(1)])
    pkmn2_ability = models.IntegerField(validators=[MaxValueValidator(293), MinValueValidator(1)])
    pkmn2_held_item = models.IntegerField(validators=[MaxValueValidator(1018), MinValueValidator(1)]) #Berries from 1 to 64, items form 65 to 1018
    pkmn2_nature = models.IntegerField(validators=[MaxValueValidator(25), MinValueValidator(1)])
    pkmn2_move1 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn2_move2 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn2_move3 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn2_move4 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])

    pkmn3_number = models.IntegerField(validators=[MaxValueValidator(807), MinValueValidator(1)])
    pkmn3_ability = models.IntegerField(validators=[MaxValueValidator(293), MinValueValidator(1)])
    pkmn3_held_item = models.IntegerField(validators=[MaxValueValidator(1018), MinValueValidator(1)]) #Berries from 1 to 64, items form 65 to 1018
    pkmn3_nature = models.IntegerField(validators=[MaxValueValidator(25), MinValueValidator(1)])
    pkmn3_move1 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn3_move2 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn3_move3 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn3_move4 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])

    pkmn4_number = models.IntegerField(validators=[MaxValueValidator(807), MinValueValidator(1)])
    pkmn4_ability = models.IntegerField(validators=[MaxValueValidator(293), MinValueValidator(1)])
    pkmn4_held_item = models.IntegerField(validators=[MaxValueValidator(1018), MinValueValidator(1)]) #Berries from 1 to 64, items form 65 to 1018
    pkmn4_nature = models.IntegerField(validators=[MaxValueValidator(25), MinValueValidator(1)])
    pkmn4_move1 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn4_move2 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn4_move3 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn4_move4 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])

    pkmn5_number = models.IntegerField(validators=[MaxValueValidator(807), MinValueValidator(1)])
    pkmn5_ability = models.IntegerField(validators=[MaxValueValidator(293), MinValueValidator(1)])
    pkmn5_held_item = models.IntegerField(validators=[MaxValueValidator(1018), MinValueValidator(1)]) #Berries from 1 to 64, items form 65 to 1018
    pkmn5_nature = models.IntegerField(validators=[MaxValueValidator(25), MinValueValidator(1)])
    pkmn5_move1 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn5_move2 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn5_move3 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn5_move4 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])

    pkmn6_number = models.IntegerField(validators=[MaxValueValidator(807), MinValueValidator(1)])
    pkmn6_ability = models.IntegerField(validators=[MaxValueValidator(293), MinValueValidator(1)])
    pkmn6_held_item = models.IntegerField(validators=[MaxValueValidator(1018), MinValueValidator(1)]) #Berries from 1 to 64, items form 65 to 1018
    pkmn6_nature = models.IntegerField(validators=[MaxValueValidator(25), MinValueValidator(1)])
    pkmn6_move1 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn6_move2 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn6_move3 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    pkmn6_move4 = models.IntegerField(validators=[MaxValueValidator(746), MinValueValidator(1)])
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="comments")
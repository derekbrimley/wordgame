from django.db import models

class Game(models.Model):
	name = models.CharField(max_length=200)

class TeamGame(models.Model):
	time_started = models.DateTimeField()
	team_1_score = models.IntegerField()
	team_2_score = models.IntegerField()

class Player(models.Model):
	username = models.CharField(max_length=100)
	games_played = models.IntegerField()
	games_won = models.IntegerField()
	games_lost = models.IntegerField()
	
class PlayerWords(models.Model):
	text = models.CharField(max_length=500)
	
class Team(models.Model):
	number_limit = models.IntegerField()
	
class PlayerTeam(models.Model):
	team_name = models.CharField(max_length=100)
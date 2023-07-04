from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Instrument(models.Model):
	instrument_name = models.CharField(max_length=100)
	def __str__(self):
        	return self.instrument_name

#class Player(models.Model):
#	player_name = models.CharField(max_length=100)
#	def __str__(self):
#        	return self.player_name


class Event(models.Model):
	event_name = models.CharField(max_length=250)
	location = models.CharField(max_length=200, blank=True)
	date = models.DateField()
	attendees = models.ManyToManyField(User,  blank=True,)
	notes = models.CharField(max_length=1000, blank=True)
	def __str__(self):
        	return self.event_name

class Piece(models.Model):
	event = models.ForeignKey(Event , null=True, blank=True, on_delete=models.CASCADE)
	piece_name = models.CharField(max_length=200, blank=True)
	composer = models.CharField(max_length=200, blank=True)
	source = models.CharField(max_length=200, blank=True) 
	number_of_parts = models.IntegerField(default=0)
	chosen_by = models.CharField(max_length=50, blank=True) 
	notes = models.CharField(max_length=1000, blank=True) 
	def __str__(self):
        	return self.piece_name

class Part(models.Model):
	piece = models.ForeignKey(Piece , null=True, on_delete=models.CASCADE)
	order = models.IntegerField(default = 0, blank=True)
	part_name = models.CharField(max_length=200, null=True, blank=True)
	instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE,  null=True, blank=True)
	player = models.ForeignKey(User, on_delete=models.CASCADE, default="Unassigned", null=True, blank=True)
	def __str__(self):
        	return self.part_name
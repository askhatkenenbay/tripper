from django.db import models
from enum import Enum
from PIL import Image
# codable, hashable???
class Follower(models.Model):
    follower_id = models.AutoField(primary_key=True)
    image = models.ImageField(default='default.jpg')
    name = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        img.save(self.image.path)

# season model
class Trip(models.Model):
    class Seasons(models.TextChoices):
        summer = 'Summer', 
        spring = 'Spring',
        fall = 'Fall', 
        winter = 'Winter',

    season = models.CharField(
        max_length=250,
        choices=Seasons.choices,
        default=Seasons.summer,
    )
    trip_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    image = models.ImageField(default='default.jpg')
    location = models.CharField(max_length=250)
    year = models.IntegerField()
    duration = models.IntegerField()

class TripFollower(models.Model):
    trip_follower_id = models.AutoField(primary_key=True)
    follower = models.ForeignKey('Follower', on_delete=models.DO_NOTHING)
    trip = models.ForeignKey('Trip', on_delete=models.DO_NOTHING)



            
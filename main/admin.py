from django.contrib import admin
from main.models import *
# Register your models here.
admin.site.site_header = 'Tripper'
admin.site.register(Follower)
admin.site.register(Trip)
admin.site.register(TripFollower)

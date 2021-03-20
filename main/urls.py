from django.urls import path
from . import views

urlpatterns = [
    path('follower/', views.getFollowers, name='GetFollowers'),
    path('follower/<int:follower_id>', views.getFollowerById, name='GetFollowerById'),
    path('seasons', views.seasons, name='seasons'),
    path('trip', views.getTrips, name='GetTrips'),
    path('trip/<int:trip_id>', views.getTripById, name='GetTripById'),
    path('image/<image_name>', views.getImage, name='GetImage'),
    path('post/follower', views.postFollower, name='postFollower'),
    path('post/trip', views.postTrip, name='postTrip'),
    path('post/followtrip', views.postTripFollow, name='postFollowTrip'),
]
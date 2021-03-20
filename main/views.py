from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from main.models import *
import json
from json import JSONEncoder
from django.core.serializers import serialize
from rest_framework import serializers
from django.conf import settings
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt

host = "https://9e97e1fd0d9a.ngrok.io/"

@csrf_exempt
def getFollowers(request):
    print("GetFollowers")
    all_pro = Follower.objects.all().values('follower_id', 'name', 'image')
    url = host + "image/"
    for temp in all_pro:
        temp['image'] = temp['image']
        temp['image'] = url + temp['image']
    return JsonResponse(list(all_pro), safe=False)

@csrf_exempt
def getFollowerById(request, follower_id):
    print("GetFollowerById")
    all_pro = Follower.objects.filter(follower_id=follower_id).all().values('follower_id', 'name', 'image')
    url = host + "image/"
    for temp in all_pro:
        temp['image'] = temp['image']
        temp['image'] = url + temp['image']
    return JsonResponse(list(all_pro), safe=False)

@csrf_exempt
def seasons(request):
    print("GetSeasons")
    data = {
        'summer': 'Summer',
        'spring': 'Spring',
        'fall': 'Fall',
        'winter': 'Winter'
    }
    return JsonResponse(data)

@csrf_exempt
def helper(fid):
    all_pro = Follower.objects.filter(follower_id=fid).all().values('follower_id', 'name', 'image')
    url = host + "image/"
    for temp in all_pro:
        temp['image'] = temp['image']
        temp['image'] = url + temp['image']
    return all_pro[0]

@csrf_exempt
def getTrips(request):
    print("GetTrips")
    url = host + "image/"
    all_pro = Trip.objects.all().values('trip_id', 'season', 'name', 'image', 'location', 'year', 'duration')
    for temp in all_pro:
        temp['image'] = temp['image'] 
        temp['image'] = url + temp['image']
        t_followers = TripFollower.objects.filter(trip_id = temp['trip_id']).all().values('follower')
        res = []
        for qwe in t_followers:
            res.append(helper(qwe['follower']))
        temp['follower'] = list(res)
    # print(sorted(list(all_pro), key=lambda x: x['follower'], reverse=True))
    # .sort(key=lambda x: )
    return JsonResponse(sorted(list(all_pro), key=lambda x: x['follower'], reverse=True), safe=False)

@csrf_exempt
def getTripById(request, trip_id):
    print("GetTripById")
    url = host + "image/"
    all_pro = Trip.objects.filter(trip_id=trip_id).all().values('trip_id', 'season', 'name', 'image', 'location', 'year', 'duration')
    for temp in all_pro:
        temp['image'] = temp['image']
        temp['image'] = url + temp['image']
        t_followers = TripFollower.objects.filter(trip_id = temp['trip_id']).all().values('follower')
        res = []
        for qwe in t_followers:
            res.append(helper(qwe['follower']))
        temp['follower'] = list(res)
    return JsonResponse(list(all_pro), safe=False)

@csrf_exempt
def getImage(request, image_name):
    print("GetImage")
    print(settings.MEDIA_ROOT)
    url = settings.MEDIA_ROOT + "/" + image_name
    print(url)
    # image_data = open(url, 'rb')
    # mbytes = image_data.read()
    # content = mbytes
    return FileResponse(open(url, 'rb'))

@csrf_exempt
def postFollower(request):
    print("PostFollower")
    fname = request.POST.get('name', None)
    fimage = request.FILES["image"]
    Follower(name=fname, image=fimage).save()
    return JsonResponse(list(), safe=False)

@csrf_exempt
def postTrip(request):
    print("PostTrip")
    tname = request.POST.get('name', None)
    tseason = request.POST.get('season', None)
    timage = request.FILES["image"]
    tlocation = request.POST.get('location', None)
    tyear = request.POST.get('year', None)
    tduration = request.POST.get('duration', None)
    Trip(name = tname, season = tseason, image = timage, location = tlocation, year = tyear, duration = tduration).save()
    return JsonResponse(list(), safe=False)


@csrf_exempt
def postTripFollow(request):
    print("Follow Trip")
    fid = request.POST.get('fid', None)
    tid = request.POST.get('tid', None)
    fff = Follower.objects.filter(follower_id = fid).first()
    ttt = Trip.objects.filter(trip_id = tid).first()
    TripFollower(follower = fff, trip = ttt).save()
    return JsonResponse(list(), safe=False)
    



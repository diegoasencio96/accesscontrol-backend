from django.shortcuts import render
from .models import Profile
from django.http import JsonResponse
# Create your views here.

def countuserprofile(request):
    data = {}
    if request.is_ajax():
        data = {
            'count': Profile.objects.count()
        }
    print(data)
    return JsonResponse(data)


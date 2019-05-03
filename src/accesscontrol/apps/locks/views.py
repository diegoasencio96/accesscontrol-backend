from django.shortcuts import render

# Create your views here.
from .models import DoorOpening
from django.http import JsonResponse
# Create your views here.

def countopening(request):
    data = {}
    if request.is_ajax():
        data = {
            'count': DoorOpening.objects.count()
        }
    print(data)
    return JsonResponse(data)

from django.urls import path
from .views import countuserprofile

urlpatterns = [
    path('total-perfiles/', countuserprofile),
]

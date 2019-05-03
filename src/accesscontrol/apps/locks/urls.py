from django.urls import path
from .views import countopening

urlpatterns = [
    path('total-registros/', countopening),
]

from .views import createCitizen
from django.urls import path, include

urlpatterns = [
    path('visitor_register/',  createCitizen, name="create_citizen"),
    
]
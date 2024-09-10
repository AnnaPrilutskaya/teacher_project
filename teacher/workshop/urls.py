from django.urls import path
from . import views

urlpatterns = [
    path('workshop', views.workshop, name='workshop'),
    path('workshop/activities', views.activities_outside_of_school, name='activities_outside_of_school'),
]
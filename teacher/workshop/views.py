from django.shortcuts import render, render_to_response
from django.template import Template, RequestContext
from .models import Activities, Documents


def workshop(request):
    template = 'workshop/workshop.html'
    return render(request, template) 

'''def activities_outside_of_school(request):
    template = 'workshop/activities.html'
    return render(request, template) '''

def activities_outside_of_school(request):
    #activitives = Activities.objects.prefetch_related('text')
    activitives = Activities.objects.all()
    #text = Documents.objects.select_related('text')
    #text = Activities.objects.get(id=1).documents.all()
    template = 'workshop/activities.html'
    return render(request, template, {'list_of_activitives': activitives}) 
    
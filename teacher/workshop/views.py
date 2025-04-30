from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.template import Template, RequestContext
from .models import Activities, Documents, Measuring_materials, Lessons


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

def measuring_materials(request):
    #activitives = Activities.objects.prefetch_related('text')
    measuring_materials = Measuring_materials.objects.all()
    #text = Documents.objects.select_related('text')
    #text = Activities.objects.get(id=1).documents.all()
    template = 'workshop/measuring_materials.html'
    return render(request, template, {'list_of_measuring_materials': measuring_materials}) 

def lessons(request):
    #activitives = Activities.objects.prefetch_related('text')
    lessons = Lessons.objects.all()
    #text = Documents.objects.select_related('text')
    #text = Activities.objects.get(id=1).documents.all()
    template = 'workshop/lessons.html'
    return render(request, template, {'list_of_lessons': lessons})
    
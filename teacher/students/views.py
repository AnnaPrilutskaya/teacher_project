from django.shortcuts import render
from .models import Articles, Memos, Recommendations
from django.views.generic import DeleteView

def index(request):
    template = 'students/index.html'
    return render(request, template) 

def student(request):
    for_students = Articles.objects.all()
    mem = Memos.objects.all()
    recom = Recommendations.objects.all()
    template = 'students/student.html'
    return render(request, template, {'article': for_students, 'new_mem': mem, 'new_recom': recom}) 

class ForStudentView(DeleteView):
    model = Articles
    template_name= 'students/detail.html'
    context_object_name = 'article'

def memo(request):
    memos = Memos.objects.all()
    template = 'students/memo.html'
    return render(request, template, {'list_of_memos': memos}) 

def recommendation(request):
    recommendations = Recommendations.objects.all()
    template = 'students/recommendation.html'
    return render(request, template, {'list_of_recommendations': recommendations})
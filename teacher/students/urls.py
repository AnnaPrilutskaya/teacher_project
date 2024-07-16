from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('student', views.student, name='student'),
    path('student/<int:pk>', views.ForStudentView.as_view(), name = 'student-detail'),
    path('student/memo', views.memo, name='memo'),
    path('student/recommendation', views.recommendation, name='recommendation'),
]
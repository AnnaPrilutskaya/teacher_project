from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('student', views.student, name='student'),
    path('student/<int:pk>', views.ForStudentView.as_view(), name = 'student-detail'),
    path('student/memo', views.memo, name='memo'),
    path('student/recommendation', views.recommendation, name='recommendation'),
    path('students/game/', views.math_game, name='math_game'),  # Главная страница
    path('students/check-answer/', views.check_answer, name='check_answer'),  # Проверка ответа
    path('students/new-problem/', views.get_new_problem, name='new_problem'),  # Новый пример
]
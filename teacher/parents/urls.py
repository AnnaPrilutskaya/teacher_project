from django.urls import path, include
from . import views

urlpatterns = [
    path('parent', views.parent, name='parent'),
    path('parent/recommendation', views.recommendation, name='recommendation'),
    #path('parent/test/', views.test_view, name='test'),
    path('parent/tests/', views.test_list, name='test_list'),
    path('parent/test/<int:test_id>/', views.test_view, name='test_detail'),
]
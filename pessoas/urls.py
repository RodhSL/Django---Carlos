from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pessoa_id>/', views.detail, name='detail'),
    path('excluir/<int:pessoa_id>/', views.excluir, name='excluir'),
    path('criar/', views.criar, name='criar'),
    path('editar/<int:pessoa_id>/', views.editar, name='editar'),
    
    path('template/', views.template, name="template")
]
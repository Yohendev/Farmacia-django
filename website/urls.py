from django.urls import path
from . import views

urlpatterns = [
    path('estoque/', views.estoque, name='estoque'),
    path('estoque/novo/', views.criar_medicamento, name='criar_medicamento'),
    path('estoque/editar/<int:pk>/', views.editar_medicamento, name='editar_medicamento'),
    path('estoque/excluir/<int:pk>/', views.excluir_medicamento, name='excluir_medicamento'),
]
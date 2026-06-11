from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estoque/', views.estoque, name='estoque'),
    path('estoque/novo/', views.criar_medicamento, name='criar_medicamento'),
    path('estoque/editar/<int:pk>/',
         views.editar_medicamento, name='editar_medicamento'),
    path('estoque/excluir/<int:pk>/',
         views.excluir_medicamento, name='excluir_medicamento'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('chatbot/', views.chatbot, name='chatbot'),
]

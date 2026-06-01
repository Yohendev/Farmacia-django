from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Medicamento
from .forms import MedicamentoForm

def home(request):
    return render(request, 'website/index.html')

@login_required(login_url='login')
def estoque(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'website/painel.html', {'medicamentos': medicamentos})

@login_required(login_url='login')
def criar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('estoque')
    return render(request, 'website/formulario_medicamento.html')

@login_required(login_url='login')
def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, request.FILES, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('estoque')
    return render(request, 'website/formulario_medicamento.html', {'medicamento': medicamento})

@login_required(login_url='login')
def excluir_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('estoque')
    return render(request, 'website/confirmar_exclusao.html', {'medicamento': medicamento})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('estoque')
        else:
            messages.error(request, 'E-mail ou senha inválidos.')
    return render(request, 'website/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_completo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirma_senha')
        
        if senha != confirma_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'website/cadastro.html')
            
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return render(request, 'website/cadastro.html')
            
        user = User.objects.create_user(username=email, email=email, password=senha, first_name=nome)
        user.save()
        login(request, user)
        return redirect('estoque')
        
    return render(request, 'website/cadastro.html')

def logout_view(request):
    logout(request)
    return redirect('home')
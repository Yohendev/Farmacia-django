from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Medicamento
from .forms import MedicamentoForm
from django.db.models import Q

def home(request):
    return render(request, 'website/index.html')

@login_required(login_url='login')
def estoque(request):
    query = request.GET.get('q')
    
    if query:
        medicamentos = Medicamento.objects.filter(
            Q(nome__icontains=query) | Q(apresentacao__icontains=query)
        )
    else:
        medicamentos = Medicamento.objects.all()
        
    return render(request, 'website/painel.html', {'medicamentos': medicamentos})

@login_required(login_url='login')
def criar_medicamento(request):
    form = MedicamentoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('estoque')
    return render(request, 'website/formulario_medicamento.html', {'form': form})

@login_required(login_url='login')
def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    form = MedicamentoForm(request.POST or None, request.FILES or None, instance=medicamento)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('estoque')
    return render(request, 'website/formulario_medicamento.html', {'form': form, 'medicamento': medicamento})

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

@login_required(login_url='login')
def relatorios(request):
    medicamentos = Medicamento.objects.all()
    
    total_produtos = medicamentos.count()
    valor_total = sum(item.preco * item.quantidade for item in medicamentos)
    estoque_baixo = medicamentos.filter(quantidade__lt=10, quantidade__gt=0).count()
    esgotados = medicamentos.filter(quantidade=0).count()
    
    contexto = {
        'total_produtos': total_produtos,
        'valor_total': valor_total,
        'estoque_baixo': estoque_baixo,
        'esgotados': esgotados,
    }
    
    return render(request, 'website/relatorios.html', contexto)

@login_required(login_url='login')
def vender_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    
    if medicamento.quantidade > 0:
        medicamento.quantidade -= 1
        
        if medicamento.quantidade == 0:
            medicamento.em_estoque = False
            
        medicamento.save()
        
    return redirect('estoque')
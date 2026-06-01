from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento
from .forms import MedicamentoForm

def estoque(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'website/estoque.html', {'medicamentos': medicamentos})

def criar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('estoque')
    
    return render(request, 'website/formulario_medicamento.html')

def editar_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, request.FILES, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('estoque')
            
    return render(request, 'website/formulario_medicamento.html', {'medicamento': medicamento})

def excluir_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    
    if request.method == 'POST':
        medicamento.delete()
        return redirect('estoque')
        
    return render(request, 'website/confirmar_exclusao.html', {'medicamento': medicamento})
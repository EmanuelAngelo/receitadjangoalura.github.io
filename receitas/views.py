from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita
def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
                               ##ordena por data mais recente, tem um filtro de publicada ou nao
    dados = {
        'receitas': receitas
    }
    
    return render(request,'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }

    return render(request,'receita.html', receita_a_exibir)

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita_icontains=nome_a_buscar)
    return render(request, 'buscar.html')
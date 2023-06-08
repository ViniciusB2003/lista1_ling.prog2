from .models import Teste
from django.shortcuts import render

# Create your views here.
def index(request):
    lista_principais = Teste.objects.order.by('nome_text')
    context = {'lista_principais': lista_principais}
    return render(request, 'menu/index.html', context)


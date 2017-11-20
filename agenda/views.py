#-*- encoding: utf-8 -*-

from django.http import HttpResponse
from models import ItemAgenda
from forms import FormItemAgenda
from django.template import RequestContext

def lista(request):
	lista_itens = ItemAgenda.objects.all()
	return render_to_response("lista.html", {'lista_itens':lista_itens})


def adiciona(request):
	form = FormItemAgenda()
	return render_to_response("adiciona.html", {'form':form}, context_instance=RequestContext(request)) #recebe objeto form instanciado acima

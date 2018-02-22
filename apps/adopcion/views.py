
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Views basadas en funciones
def  index_adopcion (request):
	return HttpResponse("index_adopcion")
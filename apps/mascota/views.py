from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

#Views basadas en funciones
def index(request):
	return render(request, 'mascota/index.html')
#Views basadas en funciones
def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_list')			
	else:
		form = MascotaForm()
	return render(request, 'mascota/mascota_form.html', {'form':form})
#Views basadas en funciones
def mascota_list(request):
	mascota= Mascota.objects.all().order_by('id')
	contexto = {'mascotas':mascota}
	return render(request,'mascota/mascota_list.html', contexto)
#Views basadas en funciones
def mascota_edit (request, id_mascota):
	mascota=Mascota.objects.get(id=id_mascota)
	if request.method=='GET':
		form = MascotaForm(instance=mascota)
	else:
		form=MascotaForm(request.POST,instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	return render (request,'mascota/mascota_form.html',{'form':form})
#Views basadas en funciones
def mascota_delete(request,id_mascota):
	mascota=Mascota.objects.get(id=id_mascota)
	if request.method=='POST':
		mascota.delete()
		return redirect('mascota:mascota_listar')
	return render (request,'mascota/mascota_delete.html',{'mascota':mascota})


#Views basadas en clases
class MascotaList(ListView):
	model = Mascota
	Template_name = 'mascota/mascota_list.html'

#Views basadas en clases
class MascotaCreate(CreateView):
	model= Mascota
	form_class = MascotaForm
	Template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')

#Views basadas en clases
class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	Templete_name =  'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')

#Views basadas en clases
class MascotaDelete(DeleteView):
	model= Mascota
	Templete_name =  'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')		



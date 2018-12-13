from django.shortcuts import render , redirect, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django import forms
from .forms import perfilformulario
from django.views.generic import View, CreateView, UpdateView, DeleteView
from .models import Perfil
from facepy import GraphAPI

#def index(request):
#    return render(request, 'blog/nos.html')
# Create your views here.

def home(request):
	graph = GraphAPI('EAANqe5z7HqMBAMZAynkwXBU15gThaCV55UbSw6bjNg3FiwwQW3WGb3eAVPbYdspDjVDp2yJdY5yZBZCFmhoz1FWfCVtXNnVaWgyGNJTTN2nwsnsEKbZCb9aXmIXWVBsJlF3Qs1REevI8daOH9TrGsuKLgMbUdtIhAWabXQV0wvNNTbbBMkhZAFH24aKvefk4ZD')
	politica = ['lula', 'Jaburu', 'aiai', 'haddad', 'Brasil', 'povo', 'comunistas', '#elenao', 'Guedes', 'pobres', 'Temer', '#elenunca']
	posts = graph.get('me/posts')
	p = []
	interessePolitica = []
	for i in range(len(posts['data'])):
		if 'message' in posts['data'][i].keys():
			p.append(posts['data'][i]['message'])

	for i in politica:
		for j in p:
			if i in j:
				interessePolitica.append(j)

	p = Perfil()
	p.perfil_usuario = graph
	p.perfil_mensagem = j
	p.save()
	return render(request, 'home/home.html', {'interessePolitica':interessePolitica}, {'politica': politica})
	#return HttpResponse(interessePolitica)
##3b5998
class perfilformulario(View): 
	form_class = perfilformulario
	template_name = 'home/home.html'

	#Pegando do banco de dados
	def get(self, request):
		form = self.form_class(None)
		perfil = Perfil.objects.all()
		return render(request, self.template_name, {'form':form, 'perfil':perfil})

	#colocando no banco de dados
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			perfil = form.save(commit=False)
			perfil.save()
			perfil.perfil_usuario = form.cleaned_data['perfil_usuario']
			perfil.save()
			return redirect('home')

		return render(request, self.template_name, {'form':form})

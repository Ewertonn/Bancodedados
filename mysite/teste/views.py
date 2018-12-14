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
	perfis = Perfil.objects.filter(perfil_id= 194)
	print(perfis)
	#https://developers.facebook.com/tools/explorer entre nesse link e pegue o token rs
	graph = GraphAPI('EAANqe5z7HqMBADqLetRWszNPTAbnfvxrELlhy3VuNHNHbxmiOJfGRtSUZAx7KvibptHYJoEEnNj65aMl4pOn1BI72spbtfmXL1T2mgageXVvcvQRctQa2Jlv4oR2GpFVisjAEcVRmiHa5lyEIcdSWJZCdkP46nJFOuwC2bUdXRfOdJcGDn7iDxPZBZBecQYZD')
	politica = ['lula', 'Jaburu', 'aiai', 'na', 'haddad', 'Brasil', 'povo', 'comunistas', '#elenao', 'Guedes', 'pobres', 'Temer', '#elenunca']
	posts = graph.get('me/posts')
	p = []
	interessePolitica = []

	for i in range(len(posts['data'])):
		if 'message' in posts['data'][i].keys():
			p.append(posts['data'][i]['message'])

	for i in politica:
		for j in p:
			if i in j:
				if j not in interessePolitica:
					interessePolitica.append(j)

	p = Perfil()
	p.perfil_usuario = graph
	p.Perfil_interesse = politica
	p.perfil_mensagem = interessePolitica
	p.save()
	return render(request, 'home/home.html', {'perfis':perfis, 'interessePolitica':interessePolitica}, {'politica': politica})
def alunos(request):
    return render(request, 'home/fotos.html')

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

from .models import Perfil
from django import forms
from django.forms import ModelForm

class perfilformulario(forms.ModelForm):
	#Motorista_senha = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Perfil
		fields = ['perfil_usuario']
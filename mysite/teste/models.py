from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	perfil_id = models.AutoField(primary_key=True)
	perfil_usuario = models.CharField(max_length=1000)
	perfil_mensagem = models.CharField(max_length=1000, default="")
	Perfil_interesse = models.CharField(max_length=1000, default="")
	
# Create your models here.

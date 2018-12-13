from django.contrib import admin
from teste.models import Perfil

class PerfilAdmin(admin.ModelAdmin):
	model = Perfil
	list_display = ['perfil_usuario'] #list_display = ['Usuario_nome','Usuario_contato']
	search_fields = ['perfil_usuario'] #search_fields = ['Usuario_nome']
	save_on_top = True
admin.site.register(Perfil, PerfilAdmin )

# Register your models here.

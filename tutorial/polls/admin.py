from django.contrib import admin

# Register your models here.
from polls.models import Contato, Pergunta, Escolha, Teste

admin.site.register(Contato)
admin.site.register(Pergunta)
admin.site.register(Escolha)
admin.site.register(Teste)
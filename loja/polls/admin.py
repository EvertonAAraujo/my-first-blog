from django.contrib import admin
from .models import Question, Choice, Cliente, Produto, Venda

#admin.site.register(Question)
#admin.site.register(Choice)

class VendaAdmin(admin.ModelAdmin):
    raw_id_fields = ['cliente', 'produto']
    list_display = ['cliente', 'produto', 'quantidade', 'valor', 'data']
    readonly_fields = ['valor']


class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ['produto']

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nome']


admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

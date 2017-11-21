from django.contrib import admin
from django.contrib.admin.templatetags.admin_list import date_hierarchy

from .models import Question, Choice, Cliente, Produto, Venda

#admin.site.register(Question)
#admin.site.register(Choice)

class VendaAdmin(admin.ModelAdmin):
    #raw_id_fields = ['cliente', 'produto']#mostra por id os campos
    list_display = ['cliente', 'produto', 'quantidade', 'valor', 'data', 'atualizacao']#campos exibidos na pagina de venda
    list_display_links = ['produto', 'cliente']#campos que são links para editar a venda
    list_editable = ['quantidade']#edita o campo direto na tela. O Campo não pode ser link
    readonly_fields = ['valor']
    readonly_fields = ['atualizacao']
    list_filter = ['cliente', 'produto']
    list_per_page = 3 #lista a quantidade de resultados por pagina
    ordering = readonly_fields
    preserve_filters = False
    #radio_fields = {"grupo": admin.VERTICAL}

class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ['produto']

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    save_as = True#Se true salva como novo em vez de editar
    save_on_top = True


admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

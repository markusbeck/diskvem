from django.contrib import admin
from tele.models import Empresa, Bairro, Cidade, Estado, Pais, Contato, Categoria, Tag, Telefone, Pagamento

class EmpresaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}
    
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Bairro)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Pais)
admin.site.register(Contato)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Telefone)
admin.site.register(Pagamento)

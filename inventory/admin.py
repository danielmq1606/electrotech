"""
Configuración del panel de administración para inventory.
"""

from django.contrib import admin
from .models import Categoria, Componente


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Componente)
class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'marca', 'modelo', 'serial', 'cantidad', 'ubicacion', 'fecha_ingreso')
    list_filter = ('categoria', 'marca')
    search_fields = ('nombre', 'serial', 'modelo', 'marca')
    ordering = ('categoria', 'nombre')
    readonly_fields = ('fecha_ingreso', 'fecha_actualizacion')

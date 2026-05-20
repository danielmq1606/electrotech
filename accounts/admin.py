"""
Configuración del panel de administración de Django para la app 'accounts'.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """
    Configuración personalizada para mostrar el campo 'rol' en el admin de Django.
    """
    list_display = ('email', 'username', 'rol', 'is_active', 'date_joined')
    list_filter = ('rol', 'is_active', 'is_staff')
    search_fields = ('email', 'username')
    ordering = ('-date_joined',)
    
    # Campos en el formulario de edición
    fieldsets = UserAdmin.fieldsets + (
        ('Rol en ElectroTech', {
            'fields': ('rol',),
        }),
    )
    
    # Campos al crear un nuevo usuario
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol en ElectroTech', {
            'fields': ('rol',),
        }),
    )

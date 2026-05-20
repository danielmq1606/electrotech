"""
Configuración del panel de administración para movements.
"""

from django.contrib import admin
from .models import Movimiento, DetalleMovimiento


class DetalleMovimientoInline(admin.TabularInline):
    """Muestra los detalles dentro del formulario de Movimiento."""
    model = DetalleMovimiento
    extra = 0
    readonly_fields = [
        'snapshot_nombre', 'snapshot_categoria', 'snapshot_marca',
        'snapshot_modelo', 'snapshot_serial', 'snapshot_detalles', 'snapshot_ubicacion'
    ]


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('numero_planilla', 'tipo', 'fecha_hora', 'usuario', 'nombre_persona')
    list_filter = ('tipo', 'fecha_hora')
    search_fields = ('numero_planilla', 'nombre_persona', 'usuario__email')
    ordering = ('-fecha_hora',)
    readonly_fields = ('numero_planilla', 'fecha_hora')
    inlines = [DetalleMovimientoInline]


@admin.register(DetalleMovimiento)
class DetalleMovimientoAdmin(admin.ModelAdmin):
    list_display = ('movimiento', 'componente', 'cantidad')
    list_filter = ('movimiento__tipo',)
    search_fields = ('componente__nombre', 'movimiento__numero_planilla')

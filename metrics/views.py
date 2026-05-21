"""
Vistas de la aplicación 'metrics'.
Dashboard principal, métricas con gráficas e historial de movimientos.
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.decorators import admin_required


@login_required
def dashboard(request):
    """Dashboard principal con accesos a todos los módulos."""
    return render(request, 'metrics/dashboard.html')


@login_required
@admin_required
def metricas_graficas(request):
    """Página de métricas con gráfica de ingresos/egresos por mes."""
    return render(request, 'metrics/graficas.html')


@login_required
@admin_required
def api_datos_grafica(request):
    """API: retorna datos JSON para la gráfica Chart.js."""
    pass


@login_required
@admin_required
def historial(request):
    """Historial completo de movimientos (ingresos y egresos)."""
    return render(request, 'metrics/historial.html')


@login_required
@admin_required
def ver_planilla_historica(request, pk):
    """Vista de una planilla histórica (re-generada desde snapshot)."""
    return render(request, 'metrics/ver_planilla.html')

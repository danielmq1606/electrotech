"""
Vistas de la aplicación 'metrics'.
Dashboard principal, métricas con gráficas e historial de movimientos.
"""

from django.shortcuts import render


def dashboard(request):
    """Dashboard principal con accesos a todos los módulos."""
    return render(request, 'metrics/dashboard.html')


def metricas_graficas(request):
    """Página de métricas con gráfica de ingresos/egresos por mes."""
    return render(request, 'metrics/graficas.html')


def api_datos_grafica(request):
    """API: retorna datos JSON para la gráfica Chart.js."""
    pass


def historial(request):
    """Historial completo de movimientos (ingresos y egresos)."""
    return render(request, 'metrics/historial.html')


def ver_planilla_historica(request, pk):
    """Vista de una planilla histórica (re-generada desde snapshot)."""
    return render(request, 'metrics/ver_planilla.html')

"""
Context processors globales para el proyecto ElectroTech.
Proporciona datos disponibles en TODOS los templates automáticamente.
"""


def datos_globales(request):
    """
    Agrega datos globales al contexto de todos los templates.
    Incluye conteo de componentes con bajo stock para alertas en el menú.
    
    La importación del modelo se hace dentro de la función (lazy import)
    para evitar errores durante migraciones iniciales cuando la tabla no existe aún.
    """
    contexto = {}
    
    if request.user.is_authenticated:
        try:
            from inventory.models import Componente
            stock_bajo_count = Componente.objects.filter(
                cantidad__lte=3,
                cantidad__gt=0
            ).count()
            contexto['stock_bajo_count'] = stock_bajo_count
            contexto['hay_stock_bajo'] = stock_bajo_count > 0
        except Exception:
            # Si la tabla no existe aún (primera migración), ignorar silenciosamente
            contexto['stock_bajo_count'] = 0
            contexto['hay_stock_bajo'] = False
    
    return contexto

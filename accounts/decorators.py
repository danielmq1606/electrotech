"""
Decoradores de permisos para la aplicación 'accounts'.
Controla el acceso a vistas según el rol del usuario (super-admin o admin).
"""

from django.shortcuts import redirect
from django.contrib import messages


def super_admin_required(view_func):
    """
    Decorador que restringe el acceso a vistas exclusivas del super-admin.
    Si el usuario no es super-admin, muestra un mensaje y redirige al dashboard.
    """
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        
        if request.user.rol != 'super_admin':
            messages.error(
                request,
                'Acceso denegado. Solo el Super Administrador puede realizar esta acción.'
            )
            return redirect('metrics:dashboard')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper


def admin_required(view_func):
    """
    Decorador que restringe el acceso a usuarios autenticados con algún rol
    (super-admin o admin). Si no tiene rol permitido, muestra error 403.
    """
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        
        if request.user.rol not in ['super_admin', 'admin']:
            messages.error(
                request,
                'Acceso denegado. No tiene permisos para acceder a esta sección.'
            )
            return redirect('accounts:permiso_denegado')
        
        return view_func(request, *args, **kwargs)
    
    return wrapper

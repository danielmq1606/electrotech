"""
Vistas de la aplicación 'accounts'.
Autenticación (login, logout) y gestión de usuarios administradores.
Solo el super-admin puede crear administradores y cambiar contraseñas.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import LoginForm, CrearAdminForm, CambiarPasswordForm
from .decorators import super_admin_required


def login_view(request):
    """
    Vista de inicio de sesión.
    Autentica al usuario con correo electrónico y contraseña.
    Si el usuario ya está autenticado, redirige al dashboard.
    """
    if request.user.is_authenticated:
        return redirect('metrics:dashboard')
    
    form = LoginForm(request, data=request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            usuario = form.get_user()
            auth_login(request, usuario)
            messages.success(request, f'¡Bienvenido, {usuario.email}! Ha iniciado sesión correctamente.')
            
            # Redirigir a la página que intentaba visitar, o al dashboard
            next_url = request.GET.get('next', 'metrics:dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Credenciales incorrectas. Verifique su correo y contraseña.')
    
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    """
    Cierra la sesión del usuario y redirige al login.
    """
    email = request.user.email
    auth_logout(request)
    messages.info(request, f'Sesión de {email} cerrada correctamente.')
    return redirect('accounts:login')


@login_required
@super_admin_required
def crear_admin(request):
    """
    Panel exclusivo del super-admin para crear cuentas de administrador.
    """
    form = CrearAdminForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            nuevo_admin = form.save()
            messages.success(
                request,
                f'Administrador {nuevo_admin.email} creado exitosamente. Ya puede iniciar sesión.'
            )
            return redirect('accounts:crear_admin')
        else:
            messages.error(request, 'Error al crear el administrador. Revise los datos ingresados.')
    
    # Listar administradores existentes
    admins = Usuario.objects.filter(rol='admin').order_by('-date_joined')
    return render(request, 'accounts/crear_admin.html', {
        'form': form,
        'admins': admins,
    })


@login_required
@super_admin_required
def cambiar_password(request):
    """
    Panel exclusivo del super-admin para cambiar la contraseña de un administrador.
    """
    form = CambiarPasswordForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            nueva_password = form.cleaned_data['nueva_password']
            usuario.set_password(nueva_password)
            usuario.save()
            messages.success(
                request,
                f'Contraseña de {usuario.email} actualizada exitosamente.'
            )
            return redirect('accounts:cambiar_password')
        else:
            messages.error(request, 'Error al cambiar la contraseña. Revise los datos.')
    
    return render(request, 'accounts/cambiar_password.html', {'form': form})


def permiso_denegado(request):
    """
    Página de error cuando un usuario intenta acceder a una sección sin permisos.
    """
    return render(request, 'accounts/permiso_denegado.html', status=403)


# Importación al final para evitar referencia circular
from .models import Usuario

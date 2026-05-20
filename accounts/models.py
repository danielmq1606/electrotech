"""
Modelos de la aplicación 'accounts'.
Gestiona los usuarios del sistema con roles (super-admin y admin).
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado para ElectroTech.
    Extiende el modelo AbstractUser de Django para añadir el campo 'rol'.
    
    Atributos heredados de AbstractUser:
        - username
        - first_name, last_name
        - email
        - password
        - is_active, is_staff, is_superuser
        - date_joined, last_login
    """
    
    class Rol(models.TextChoices):
        """Roles disponibles en el sistema."""
        SUPER_ADMIN = 'super_admin', 'Super Administrador'
        ADMIN = 'admin', 'Administrador'
    
    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.ADMIN,
        verbose_name='Rol del usuario',
        help_text='Define los permisos del usuario en la plataforma.'
    )
    
    # Usar email como campo de autenticación principal
    email = models.EmailField(
        unique=True,
        verbose_name='Correo electrónico',
        help_text='Dirección de correo utilizada para iniciar sesión.'
    )
    
    USERNAME_FIELD = 'email'          # Login con correo electrónico
    REQUIRED_FIELDS = ['username']    # Campo requerido al crear superusuarios
    
    def __str__(self):
        return f"{self.email} ({self.get_rol_display()})"
    
    @property
    def es_super_admin(self):
        """Retorna True si el usuario es super administrador."""
        return self.rol == self.Rol.SUPER_ADMIN
    
    @property
    def es_admin(self):
        """Retorna True si el usuario es administrador."""
        return self.rol == self.Rol.ADMIN
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-date_joined']

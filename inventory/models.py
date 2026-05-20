"""
Modelos de la aplicación 'inventory'.
Gestiona las categorías y los componentes del almacén.
"""

from django.db import models


class Categoria(models.Model):
    """
    Categoría de componente de hardware.
    Ejemplos: Procesadores, Tarjetas madre, Memorias RAM, etc.
    """
    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nombre de la categoría',
        help_text='Nombre único que identifica la categoría (ej: "Procesadores").'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']


class Componente(models.Model):
    """
    Componente de hardware registrado en el inventario del almacén.
    Cada componente pertenece a una categoría y tiene un stock controlado.
    """
    nombre = models.CharField(
        max_length=200,
        verbose_name='Nombre del componente',
        help_text='Nombre descriptivo del componente (ej: "Tarjeta gráfica NVIDIA RTX 4060").'
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='componentes',
        verbose_name='Categoría',
        help_text='Categoría a la que pertenece este componente.'
    )
    marca = models.CharField(
        max_length=100,
        verbose_name='Marca',
        help_text='Fabricante del componente (ej: "NVIDIA", "AMD", "Intel").'
    )
    modelo = models.CharField(
        max_length=100,
        verbose_name='Modelo',
        help_text='Modelo específico del componente (ej: "RTX 4060 6GB").'
    )
    serial = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Número de serie',
        help_text='Identificador único del componente. No puede estar vacío ni repetirse.'
    )
    detalles = models.TextField(
        blank=True,
        verbose_name='Detalles o especificaciones',
        help_text='Información adicional: capacidad, velocidad, tipo de conexión, etc.'
    )
    cantidad = models.PositiveIntegerField(
        default=0,
        verbose_name='Cantidad disponible',
        help_text='Unidades disponibles actualmente en el almacén.'
    )
    ubicacion = models.CharField(
        max_length=100,
        verbose_name='Ubicación en el almacén',
        help_text='Posición física dentro del almacén (ej: "Estante A1", "Sección B3").'
    )
    imagen = models.ImageField(
        upload_to='componentes/',
        blank=True,
        null=True,
        verbose_name='Imagen del componente',
        help_text='Fotografía o ilustración del componente. Opcional.'
    )
    fecha_ingreso = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de ingreso',
        help_text='Fecha en que se registró por primera vez en el sistema.'
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de última actualización'
    )
    
    def __str__(self):
        return f"{self.nombre} - {self.marca} {self.modelo} ({self.cantidad} uds.)"
    
    @property
    def stock_bajo(self):
        """Retorna True si el componente tiene 3 unidades o menos."""
        return 0 < self.cantidad <= 3
    
    @property
    def agotado(self):
        """Retorna True si no hay unidades disponibles."""
        return self.cantidad == 0
    
    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        ordering = ['categoria', 'nombre']
        indexes = [
            models.Index(fields=['serial']),
            models.Index(fields=['categoria']),
        ]

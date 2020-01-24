from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="nombre clave", max_length=200, unique=True)
    #SlugField es para claves alfanumericas, no puede poner espacios. Queda a modo de espacio
    name = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name
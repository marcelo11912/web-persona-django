from django.db import models
from stdimage import StdImageField


# Create your models here.
class Proyecto (models.Model):
    titulo = models.CharField(max_length=200,verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    imagen = StdImageField(upload_to='media')
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    link = models.URLField(null=True,blank=True)
    
    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        ordering = ["-creacion"]
  
    def __str__(self):
        return self.titulo
    



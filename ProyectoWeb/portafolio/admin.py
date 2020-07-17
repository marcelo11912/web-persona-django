from django.contrib import admin
from .models import Proyecto

# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields = ['creacion', 'actualizacion']

admin.site.register(Proyecto,ProyectoAdmin)

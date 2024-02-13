from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    # Personaliza la configuración del modelo User si es necesario
    pass

# Register your models here.
admin.site.register(Estado)
admin.site.register(Ubicacion)
admin.site.register(Uom)
admin.site.register(Owner)
admin.site.register(Ficha)
admin.site.register(Condicion)
admin.site.register(Clasificacion)
admin.site.register(Bodega)
admin.site.register(Origen)
admin.site.register(Comat)
admin.site.register(Incoming)
admin.site.register(Detalle_Incoming)
admin.site.register(Estado_Repuesto)
admin.site.register(Consumos)
#admin.site.register(Categotia_incoming)
admin.site.register(Compania)
admin.site.register(Cargo)
admin.site.register(Consumidor)
admin.site.register(Licencia)






from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "telefono", "creado")
    search_fields = ("nombre", "email", "telefono")
    list_filter = ("creado",)
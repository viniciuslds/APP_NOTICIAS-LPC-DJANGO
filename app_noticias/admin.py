from django.contrib import admin
from .models import Noticia
# Register your models here.
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass
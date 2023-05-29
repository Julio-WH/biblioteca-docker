from django.contrib import admin
from apps.Libro.models import Libro
# Register your models here.

# @admin.register(Libro)
# class LibroAdmin(admin.ModelAdmin):
#     model = Libro

admin.site.register(Libro)

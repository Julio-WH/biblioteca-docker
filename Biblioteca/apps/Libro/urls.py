from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.Libro.views import lista_libro

urlpatterns = [
    path('lista/', login_required(lista_libro), name='lista_libro'),
]
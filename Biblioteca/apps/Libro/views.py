from django.shortcuts import render
from apps.Libro.models import Libro

# Create your views here.


def lista_libro(request):
    q_libros = Libro.objects.all()
    context = {
        'libros':q_libros
    }
    return render(request, 'lista_libros.html', context)
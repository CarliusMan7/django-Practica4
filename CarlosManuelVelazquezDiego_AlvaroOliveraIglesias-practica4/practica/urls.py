from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

# Vista para la página de inicio
def home(request):
    return JsonResponse({"message": "Bienvenido a la API de la Biblioteca. Usa /api/ para acceder a los endpoints."})

urlpatterns = [
    path('', home),  # Ruta para la página de inicio
    path('admin/', admin.site.urls),
    path('api/', include('primerapp.urls')),
]


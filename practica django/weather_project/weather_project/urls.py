from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("tiempo/", include("weather.urls"))
    # include el nombre de la aplicacion
    # rutas generales
]

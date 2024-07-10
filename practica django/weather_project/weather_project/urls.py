from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("app/", include("weather.urls"))
    # include el nombre de la aplicacion
    # rutas generales
]

from django.urls import path
import weather.views as views

urlpatterns = [
     path("", views.hola_mundo)

]

#  path("hola-mundo/", views.hola_mundo)
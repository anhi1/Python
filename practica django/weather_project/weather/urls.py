from django.urls import path
import weather.views as views

urlpatterns = [
     path("hola-mundo/", views.hola_mundo)

]

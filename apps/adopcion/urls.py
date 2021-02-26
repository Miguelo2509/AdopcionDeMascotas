from django.urls import path
from apps.adopcion.views import index

#urls de la aplicacion

urlpatterns = [
    path('', index),
]
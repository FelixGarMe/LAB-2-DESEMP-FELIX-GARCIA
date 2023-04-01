from django.contrib import admin
from django.urls import include, path

ulrpatterns = [
    path('encuesta/',include('encuesta.urls')),
    path('admin/', admin.site.urls),
]
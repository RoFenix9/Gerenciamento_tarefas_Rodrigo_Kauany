from django.contrib import admin
from django.urls import path, include
from tarefas.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('tarefas/', include('tarefas.urls')),
    path('usuarios/', include('usuarios.urls')),
]
import json

from time import time
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from django.core.serializers import serialize
from django.http import HttpResponse,JsonResponse

from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView,DetailView
from django.urls import reverse_lazy

from .models import *
from django.contrib import messages

def home(request):
    
    return render(request, 'social/home.html')

def index(request):
    
    return render(request, 'social/index.html')

def registro(request):
    
    return render(request, 'social/registro.html')

def somos(request):
    
    return render(request, 'social/somos.html')

def tienda(request):
    
    return render(request, 'social/tienda.html')
def contactanos(request):
    
    return render(request, 'social/contactanos.html')
# Create your views here.


#Django viene con un sistema de autenticación de usuario incorporado.
# Esta configuración realiza los requisitos más comunes que necesita el proyecto,
# manejando una amplia gama de tareas y contraseñas y permisos válidos.
# Podemos crear el inicio de sesión de usuario importando módulos de autenticación de usuario.
# userCreationForm, se utiliza para crear un nuevo usuario.
# Es un módulo integrado heredado de la clase ModelForm.



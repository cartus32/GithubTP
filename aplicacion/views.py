from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def inicio(request):
    return HttpResponse("Trabajo Practico N°2, Taller de Prog.")
    
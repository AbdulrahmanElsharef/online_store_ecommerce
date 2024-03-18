
# Create your views here.
from django.shortcuts import render,get_object_or_404


def HOME (request):
    return  render ( request , 'main/home.html',{} )
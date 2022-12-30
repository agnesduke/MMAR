from django.shortcuts import render, redirect

from django.views import View
from .models import Client, Service, Category


class Home(View):
    template_name = None


# Create your views here.



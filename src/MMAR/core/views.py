from django.shortcuts import render, redirect

from django.views import View
from .models import Client, Service, Category


class Home(View):
    template_name = 'societe.html'

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

  
class ClientPage(View):
    template_name = 'client.html'

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        return render(request,self.template_name)    

class ServicesPage(View):
    template_name = 'services.html'

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        return render(request,self.template_name)    

class comptePage(View):
    template_name = 'compte.html'

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        return render(request,self.template_name)    

class compte(View):
    template_name = 'compte.html'

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        return render(request,self.template_name)            



# Create your views here.



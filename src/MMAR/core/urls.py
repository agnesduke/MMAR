from django.urls import path, include
from .views import Home,ClientView,ServicesView,AccountView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("client",ClientView.as_view(),name="client"),
    path('service',ServicesView.as_view(),name='services'),
    path('compte',AccountView.as_view(),name='compte'),
]
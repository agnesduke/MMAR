from django.urls import path, include
from .views import Home,ClientPage,ServicesPage,comptePage

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("client",ClientPage.as_view(),name="client"),
    path('service',ServicesPage.as_view(),name='services'),
    path('compte',comptePage.as_view(),name='compte'),
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("port/", views.port_endpoint, name="port_endpoint"),
]

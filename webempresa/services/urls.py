from django.urls import path
from . import views

urlpatterns = [

    #Paths del core
    path('services/', views.services, name="services"),
]
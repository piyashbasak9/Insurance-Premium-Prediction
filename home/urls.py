from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contract/', views.contract, name='contract'),
    path('prediction/', views.prediction, name='prediction'), 
    
]
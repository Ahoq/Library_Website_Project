from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'museum-home'),
    path('about/', views.about, name = 'museum-about'),
    path('hours/', views.hours, name = 'museum-hours'),
    path('ex1/', views.ex1, name = 'museum-ex1'),
    path('ex2/', views.ex2, name = 'museum-ex2'),
    path('ex3/', views.ex3, name = 'museum-ex3'),
    path('ex4/', views.ex4, name = 'museum-ex4'),
    path('map/', views.map, name = 'museum-map'),
]
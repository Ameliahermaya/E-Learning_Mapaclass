from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peluang/', views.peluang, name='peluang'),
    path('BarisandanDeret/', views.BarisandanDeret, name='BarisandanDeret'),
    path('Eksponen/', views.Eksponen, name='Eksponen'),
    path('home/', views.home, name='home'),
    path('Referensi/', views.Referensi, name='Referensi'),
    path('Statistika/', views.Statistika, name='Statistika'),
    path('LogOut/', views.LogOut, name='LogOut'),
]
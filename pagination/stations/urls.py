from django.urls import path
from . import views

app_name = 'stations'

urlpatterns = [
    path('', views.bus_stations, name='stations'),

]

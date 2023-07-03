from django.urls import path, include

urlpatterns = [
    path('bus_stations/', include('stations.urls', namespace='stations')),
]

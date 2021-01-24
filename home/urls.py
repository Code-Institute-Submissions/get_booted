from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]

if settings.DEBUG:
    urlpatterns = [
        path("404", http404),
        path("500", http500),
    ] + urlpatterns

    

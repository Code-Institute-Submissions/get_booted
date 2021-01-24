from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('', views.index, name='home')
]
if settings.DEBUG:
    urlpatterns = [
        path("404", views.http404),
        path("500", views.http500),
    ] + urlpatterns
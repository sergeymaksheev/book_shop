from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('api.catalog.urls')),
]
from django.urls import path, re_path
from django.urls import include

urlpatterns = [
    path('', include('api.catalog.urls')),
    path('', include('api.orders.urls')),
    path('drf-auf/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
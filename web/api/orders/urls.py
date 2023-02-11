from django.urls import path
from . import views

# Make your views here

urlpatterns = [
    # path('', include(router.urls)),
    path('order/', views.OrderDetailAPIView.as_view()),
    # path('order/<int:pk>/', views.OrderDetailAPIView.as_view()),
]
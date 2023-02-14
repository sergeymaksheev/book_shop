from django.urls import path
from . import views

# Make your views here

urlpatterns = [
    # path('', include(router.urls)),
    path('order/', views.OrderAPIView.as_view()),
    path('orderlist/', views.OrderListAPIView.as_view()),
    path('order/<int:pk>/status/', views.OrderStatusAPIView.as_view()),
    path('order/<int:pk>/paid/', views.OrderPaidAPIView.as_view()),
]
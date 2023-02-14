from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework import generics
from rest_framework import pagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Sum

from api.orders.serializers import *
from orders.permissions import IsAdminOrReadOnly
from orders.models import Order, OrderDetail

class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


class OrderAPIView(APIView):
    
    serializer_class = OrderResponseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        body = OrderDataSerializer(data=request.data)
        if body.is_valid(raise_exception=True):
        
            serializer = self.serializer_class(data=body.data, context={"user": self.request.user, "order": body.data})

            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(data=serializer.data, status=HTTP_201_CREATED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response(body.errors, status=HTTP_400_BAD_REQUEST)


class OrderListAPIView(generics.ListAPIView):
    
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]
        
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('id').annotate(
            total_price=Sum('order_detail__price_for_quantity')
        )
    
class OrderStatusAPIView(generics.RetrieveUpdateAPIView):

    queryset = Order.objects.select_related('user')
    serializer_class = OrderStatusSerializer
    permission_classes = [IsAdminUser]


class OrderPaidAPIView(generics.RetrieveUpdateAPIView):

    queryset = Order.objects.select_related('user')
    serializer_class = OrderPaidSerializer
    permission_classes = [IsAdminUser]


    


    
















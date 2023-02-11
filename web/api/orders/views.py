from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework import authentication
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import OrderDetailSerializer
from orders.permissions import IsAdminOrReadOnly
from orders.models import Order, OrderDetail
from catalog.models import Book, Author, Genre
from rest_framework import pagination
from rest_framework import status
from rest_framework.settings import api_settings

class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000

# class OrderAPIView(APIView):
#     permission_classes = (IsAdminOrReadOnly,)

#     def get(self, request):
#         queryset = Order.objects.all()
#         return Response (request, OrderSerializer(queryset, many=True).data)

#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({'post': serializer.data})


# class OrderListAPIView(generics.ListAPIView):
    
#     # queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     pagination_class = LargeResultsSetPagination
#     permission_classes = (IsAdminOrReadOnly,)

# class OrderCreateAPIView(generics.CreateAPIView):
    
#     # queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     pagination_class = LargeResultsSetPagination
#     permission_classes = (IsAdminOrReadOnly,)



class OrderDetailAPIView(generics.CreateAPIView):
    
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminOrReadOnly]

    def post(self, request):
        pass







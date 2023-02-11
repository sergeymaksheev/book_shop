from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from catalog.models import Book, Author, Genre, Publisher
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, PublisherSerializer
from rest_framework import pagination
from catalog.permissions import IsAdminOrReadOnly

from django.http import Http404


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()

#     serializer_class = BookSerializer
#     pagination_class = LargeResultsSetPagination
#     permission_classes = (IsAdminOrReadOnly,)

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = (IsAdminOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

class BookTitle(APIView):
    pagination_class = LargeResultsSetPagination
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request):
        title = [book.title for book in Book.objects.all()]
        return Response(title)

class BookDetail(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(id=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

#     def get(self, request):
#         queryset = Book.objects.all()
#         return Response (BookSerializer(queryset, many=True).data)

    # def post(self, request):
    #     serializer = BookSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=False)
    #     serializer.save()

    #     return Response({'post': serializer.data})

 
# class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (IsAdminOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = (IsAdminOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = (IsAdminOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = (IsAdminOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (IsAdminOrReadOnly,)

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)



    


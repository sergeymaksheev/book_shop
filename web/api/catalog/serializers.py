from rest_framework import serializers
from catalog.models import Book, Author, Genre, Publisher


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ('id', 'title', 'author', 'summary', 'isbn', 'genre', 'publisher', 'number_of_pages', 'year', 'price', 'quantity')
#         depth = 1

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    summary  = serializers.CharField()
    price = serializers.IntegerField()
    isbn = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


    # def create (self, validated_data):
    #     return Book.objects.create(**validated_data)
    


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'phone', 'email', 'city')
        depth = 1





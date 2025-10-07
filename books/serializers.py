from rest_framework import serializers

from books.models import Book

from rest_framework import serializers
from .models import Author, Genre, Publisher, Book


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'books_count']

    def get_books_count(self, obj):
        return obj.books.count()


class GenreSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ['id', 'name', 'books_count']

    def get_books_count(self, obj):
        return obj.books.count()


class PublisherSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'description', 'books_count']

    def get_books_count(self, obj):
        return obj.books.count()


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    publisher_name = serializers.CharField(source='publisher.name', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_name', 'genre', 'genre_name',
            'publisher', 'publisher_name', 'published',
            'price', 'number_of_left', 'description'
        ]
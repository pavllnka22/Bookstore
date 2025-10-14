from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book, Author, Genre, Publisher
from books.serializers import BookSerializer, AuthorSerializer, GenreSerializer, PublisherSerializer
from authentication.permissions import IsAdminUser


class AuthorList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        if author is None:
            return Response({'error': 'Author not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = Author.objects.get(pk=pk)
        if author is None:
            return Response({'error': 'Author not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = Author.objects.get(pk=pk)
        if author is None:
            return Response(
                {'error': 'Author not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        if author.books.exists():
            return Response(
                {'error': 'You cannot delete this author because there are their books in stock'},
                status=status.HTTP_400_BAD_REQUEST
            )

        author.delete()
        return Response(
            {'message': f'Author {author.name} has been deleted'},
            status=status.HTTP_200_OK)


class GenreList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        if genre is None:
            return Response({'error': 'Genre not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        if genre is None:
            return Response({'error': 'Genre not found'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        if genre is None:
            return Response(
                {'error': 'Genre not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        if genre.books.exists():
            return Response(
                {'error': 'You cannot delete this genre because there are books in this genre in stock'},
                status=status.HTTP_400_BAD_REQUEST
            )

        genre.delete()
        return Response(
            {'message': f'Genre {genre.name} has been deleted'},
            status=status.HTTP_200_OK)


class PublisherList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        publisher = Publisher.objects.get(pk=pk)
        if publisher is None:
            return Response(
                {'error': 'Publisher not found'},
            )
        if publisher.books.exists():
            return Response(
                {'error': 'You cannot delete this publisher because there are books of this publisher in stock'},
                status=status.HTTP_400_BAD_REQUEST
            )
        publisher.delete()
        return Response(
            {'message': f'Publisher {publisher.name} has been deleted'},
            status=status.HTTP_200_OK)


class PublisherDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        publisher = Publisher.objects.get(pk=pk)
        if publisher is None:
            return Response(
                {'error': 'Publisher not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)

    def put(self, request, pk):
        publisher = Publisher.objects.get(pk)
        if publisher is None:
            return Response(
                {'error': 'Publisher not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PublisherSerializer(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete(self, request, pk):
    permission_classes = [IsAdminUser]
    publisher = Publisher.objects.get(pk=pk)
    if publisher is None:
        return Response(
            {'error': 'Publisher not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    if publisher.books.exists():
        return Response(
            {'error': 'You cannot delete this publisher because there are books of this publisher in stock'},
            status=status.HTTP_400_BAD_REQUEST
        )
    publisher.delete()
    return Response(
        {'message': f'Publisher {publisher.name} has been deleted'},
        status=status.HTTP_200_OK)


class BookList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        if book is None:
            return Response(
                {'error': 'Book not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):

        book = Book.objects.get(pk=pk)
        if book is None:
            return Response(
                {'error': 'Book not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        permission_classes = [IsAdminUser]
        book = Book.objects.get(pk=pk)
        if book is None:
            return Response(
                {'error': 'Book not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        book.delete()
        return Response(
            {'message': f'Book {book.title} has been deleted'},
            status=status.HTTP_200_OK)


@api_view(['GET'])
def get_author_books(request, author_id):
    author = Author.objects.get(author_id=author_id)
    if author is None:
        return Response({'error': 'Author not found'},
                        status=status.HTTP_404_NOT_FOUND
                        )
    books = author.books.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_genre_books(request, genre_id):
    genre = Genre.objects.get(genre_id=genre_id)
    if genre is None:
        return Response({'error': 'Genre not found'},
                        status=status.HTTP_404_NOT_FOUND)
    books = genre.books.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_publisher_books(request, publisher_id):
    publisher = Publisher.objects.get(pk=publisher_id)
    if publisher is None:
        return Response({'error': 'Publisher not found'},
                        status=status.HTTP_404_NOT_FOUND
                        )
    books = publisher.books.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

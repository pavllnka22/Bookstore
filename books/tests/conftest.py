import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from books.models import Author, Book, Genre, Publisher

User = get_user_model()

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpass123')

@pytest.fixture(scope='function')
def api_client() -> APIClient:

    return APIClient()

@pytest.fixture
def api_client_authenticated(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def author(db):
    return Author.objects.create(name='Author 1', bio='Author 1')

@pytest.fixture
def author_with_books(db, author):
    genre = Genre.objects.create(name='Genre 1')
    punblisher = Publisher.objects.create(name='Publisher 1', description = 'description 1')
    Book.objects.create(title='Book 1', author=author, price=100, pages=100, published='2023-01-15', language='en',  description='Some description', number_of_left=1, in_stock=True , genre=genre, publisher=punblisher)
    return author

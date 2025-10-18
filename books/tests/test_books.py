from rest_framework import status

from books.models import Author


def test_get_author_list(api_client, author):
    Author.objects.create(name = author.name, bio = author.bio)
    response = api_client.get('/books/authors/', format='json')
    assert response.status_code == 200
    assert response.data[0]['name'] == author.name

def test_create_author(api_client_authenticated):
    data = {'name': 'New Author', 'bio': 'New Bio'}
    response = api_client_authenticated.post('/books/authors/', data)
    assert response.status_code == 201
    assert response.data['name'] == 'New Author'

def test_create_author_unauthenticated(api_client):
    data = {'name': 'New Author List'}
    response = api_client.post('/books/authors/', data)
    assert response.status_code == 401

def test_delete_author_with_books(api_client_authenticated, author_with_books):
    response = api_client_authenticated.delete(f'/books/authors/{author_with_books.id}/')
    assert response.status_code == 400

def test_update_author(api_client_authenticated, author):
    data = {'name': 'Updated Name', 'bio': 'Updated Bio'}
    response = api_client_authenticated.put(f'/books/authors/{author.id}/', data)
    assert response.status_code == 200
    assert response.data['name'] == 'Updated Name'

from django.contrib import admin
from django.urls import path

from books import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author-detail'),
    path('authors/<int:author_id>/books/', views.get_author_books, name='author-books'),

    # Genres URLs
    path('genres/', views.GenreList.as_view(), name='genre-list'),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name='genre-detail'),
    path('genres/<int:genre_id>/books/', views.get_genre_books, name='genre-books'),

    # Publishers URLs
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),

    # Books URLs
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),

]

from django.contrib import admin
from .models import Book, Author, Genre, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title',)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "bio")
    search_fields = ("name",)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

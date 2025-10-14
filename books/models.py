from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT,related_name='books')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT,related_name='books')
    publisher = models.ForeignKey(Publisher,on_delete=models.PROTECT, related_name='books')
    pages = models.IntegerField()
    published = models.DateField()
    language = models.CharField(max_length=100)
    in_stock = models.BooleanField()
    description = models.TextField(blank=True)
    number_of_left = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='books/', null=True, blank=True)




    
from django.db import models

class Author(models.Model):
    authorid=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    
class Book(models.Model):
    isbn=models.CharField(max_length=50,primary_key=True)
    title=models.CharField(max_length=50)
    author=models.ForeignKey(Author)
    publisher=models.CharField(max_length=50)
    publishDate=models.DateField(max_length=50)
    price=models.CharField(max_length=50)
    

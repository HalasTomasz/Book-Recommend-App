from email.policy import default
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models

class BookReaders(models.Model):
    Reader_ID = models.AutoField(primary_key=True,editable=False)
    Name = models.CharField(max_length=255, null = True, blank = True)
    FireBaseAuth = models.CharField(max_length=255, null = True, blank = True)
    Age = models.CharField(max_length=10, null = True, blank = True)
    Sex = models.CharField(max_length=10, null = True, blank = True)

class BookAuthor(models.Model):
    Author_ID = models.AutoField(primary_key=True,editable=False)
    Author_Name = models.CharField(max_length=255, null = True, blank = True)

    def __str__(self):
        return self.Author_Name

class Genre(models.Model):
    Genre_ID = models.AutoField(primary_key=True,editable=False)
    Genre_Name = models.CharField(max_length=255, null = True, blank = True)

class UserGenre(models.Model):
    Order_ID = models.AutoField(primary_key=True,editable=False)
    Reader_ID = models.ForeignKey(BookReaders, null = True, on_delete=models.SET_NULL) # here thnik about this 
    Genre_ID = models.ForeignKey(Genre, null = True, on_delete=models.SET_NULL) # here thnik about this 

class Book(models.Model):
    Book_ID = models.AutoField(primary_key=True,editable=False)
    Name = models.CharField(max_length=255, null = True, blank = True)
    Author = models.ForeignKey(BookAuthor, null = True, on_delete=models.SET_NULL) # here thnik about this 
    Availability =  models.IntegerField(null=True,blank=True, default=0)
    Description = models.TextField(null = True, blank = True)
    Rating = models.DecimalField(max_digits=7, decimal_places=2, null = True, blank = True)
    NumberReviews = models.IntegerField(null=True,blank=True)
    ImgSource = models.TextField(null = True, blank = True)
    Genre = models.ForeignKey(Genre, null = True, on_delete=models.SET_NULL) # here thnik about this 

    def __str__(self):
        return self.Name

class UserWantedBooks(models.Model):
    Order_ID = models.AutoField(primary_key=True,editable=False)
    Reader_ID = models.ForeignKey(BookReaders, null = True, on_delete=models.SET_NULL) # here thnik about this 
    Book_ID = models.ForeignKey(Book, null = True, on_delete=models.SET_NULL) # here thnik about this 

class Review(models.Model):
    AllReviews_ID = models.AutoField(primary_key=True, editable=False)
    Date =  models.DateTimeField(auto_now_add=True)
    Review = models.DecimalField(max_digits=7, decimal_places=2, null = True, blank = True)
    Reader_ID = models.ForeignKey(BookReaders, null = True, on_delete=models.SET_NULL) # here thnik about this 
    Book_ID = models.ForeignKey(Book, null = True, on_delete=models.SET_NULL) # here thnik about this 

class History(models.Model):
    AllRenatls_ID = models.AutoField(primary_key=True, editable=False)
    Reader_ID = models.ForeignKey(BookReaders, null = True, on_delete=models.SET_NULL) # here thnik about this 
    Date_Taken =  models.DateTimeField(auto_now_add=True)
    Book_ID = models.ForeignKey(Book, null = True, on_delete=models.SET_NULL) # here thnik about this 
    Returned = models.BooleanField(null = True)
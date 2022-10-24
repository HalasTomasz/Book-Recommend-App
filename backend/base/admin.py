from django.contrib import admin
from .models import *

admin.site.register(BookReaders)

admin.site.register(Book)

admin.site.register(BookAuthor)

admin.site.register(Genre)

admin.site.register(UserGenre)

admin.site.register(UserWantedBooks)

admin.site.register(Review)

admin.site.register(History)

# Register your models here.

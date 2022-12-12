from pickle import FALSE
from sqlite3 import Date
from tokenize import Name
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book, BookReaders, Genre, History, UserGenre, AlgorithmRecomendations, GenreShort, OFFTOP_Recomendations, Review
from .serializer import BookSerializer,BooksSerializer, BookReadersSerializer, BookGenreSerializer , GenreSerializer, HistorySerializer, AlogrithmSerializer, OFFTOPSerializer, ReviewSerializer
import datetime
# Create your views here.



@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/books/',
        '/api/books/<id>/reviews/',
        '/api/history/<uid>/',
    ]
    return Response(routes)
#######################################
'''
    BOOKS SECTION
'''
@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBook(request, pk):

    book = Book.objects.get(Book_ID=pk)
    serializer_book = BookSerializer(book, many=False)
    uid = request.query_params.get('user')
    user_obj = BookReaders.objects.get(FireBaseAuth=uid)
    data_review = Review.objects.filter(Reader_ID=user_obj, Book_ID = book).values_list('Review',flat=True)

    if len(data_review) == 0:
        newdict={'Review':None}
        newdict.update(serializer_book.data)
    else:
        newdict={'Review':data_review[0]}
        newdict.update(serializer_book.data)

    return Response(newdict)

'''
    USER SECTION
'''
@api_view(['GET'])
def getUser(request, id):
    user = BookReaders.objects.get(FireBaseAuth=id)
    serializer = BookReadersSerializer(user, many=False)
    return Response(serializer.data)    


@api_view(['PUT'])
def updateUser(request, id):
    data_user = request.data
    BookReaders.objects.filter(FireBaseAuth=id).update(Name=data_user['name'], Age=data_user['age'], Sex=data_user['sex'])
    return Response("Data updated")

@api_view(['POST'])
def registerUser(request):

    data_user = request.data
    new_user = BookReaders.objects.create(
        Name = data_user['name'],
        FireBaseAuth = data_user['uid'],
        Age = data_user['age'],
        Sex = data_user['sex'],
    )
    print(data_user['genres'])

    genres_id = GenreShort.objects.filter(Genre_Name__in=data_user['genres']).values_list('Genre_ID',flat=True)
    user_genres_types = [UserGenre(Reader_ID = new_user,Genre_ID=GenreShort.objects.get(Genre_ID=genre_id)) for genre_id in genres_id]
    UserGenre.objects.bulk_create(user_genres_types)
    print(user_genres_types)
    serializer_user = BookReadersSerializer(new_user, many=False)
    return Response(serializer_user.data)

'''
    HISTORY SECTION
'''
@api_view(['GET'])
def getUserHistory(request, user_auth_key):
    user = History.objects.get(Reader_ID=user_auth_key)
    serializer = BookReadersSerializer(user, many=False)
    return Response(serializer.data) 
       
@api_view(['POST'])
def setUserHistory(request):
    data_user = request.data
    user = BookReaders.objects.get(FireBaseAuth=data_user['uid'])
    book = Book.objects.get(Book_ID=data_user['book_id'])
    if book.Availability !=0:
        is_this_book_rentend = History.objects.filter(Reader_ID=user.Reader_ID, Book_ID=book.Book_ID).values_list('Returned',flat=True)
        if not ( False in is_this_book_rentend):
            History.objects.create(
                Reader_ID =user,
                Book_ID = book,
            )
            Book.objects.filter(Book_ID=data_user['book_id']).update(Availability=book.Availability-1)

            return Response("History added")
        return Response("Failed to add into history - already taken", status=status.HTTP_403_FORBIDDEN)
    else:
         return Response("Fialed to add into history", status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT'])
def returnBookUserHistory(request):
    data_user = request.data
    print(data_user)
    History.objects.filter(AllRenatls_ID=data_user['rent_id']).update(Returned=1)
    book = Book.objects.get(Book_ID=data_user['book_id'])
    Book.objects.filter(Book_ID=data_user['book_id']).update(Availability=book.Availability+1)

    return Response("Return Succesfull")

@api_view(['GET'])
def getUserHistory(request, id):
    user = BookReaders.objects.get(FireBaseAuth=id)
    user_hist = History.objects.filter(Reader_ID=user.Reader_ID).order_by("-Date_Taken")
    serializer = HistorySerializer(user_hist,many=True)

    return Response(serializer.data)

'''
    GENRE SECTION
'''
@api_view(['GET'])
def getShortGenre(request):
    genre = GenreShort.objects.filter()
    serializer = GenreSerializer(genre, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def getGenre(request):
    genre = Genre.objects.filter()
    serializer = GenreSerializer(genre, many=True)
    return Response(serializer.data) 
    
    
# @api_view(['GET'])
# def getUserGenre(request, id):
#     user = BookReaders.objects.get(FireBaseAuth=id)
#     genres_id = UserGenre.objects.filter(Reader_ID=user.Reader_ID).values_list('Genre_ID',flat=True)
#     genres_name =  GenreShort.objects.filter(Genre_ID__in=genres_id)
#     serializer = GenreSerializer(genres_name, many=True)
#     return Response(serializer.data) 

@api_view(['POST'])
def updateUserGenre(request):
    data_user = request.data
    print(data_user)
    user = BookReaders.objects.get(FireBaseAuth=data_user['uid'])
    UserGenre.objects.filter(Reader_ID=user.Reader_ID).delete()

    genres_id = GenreShort.objects.filter(Genre_Name__in=data_user['new_genres']).values_list('Genre_ID',flat=True)
    user_genres_types = [UserGenre(Reader_ID = user, Genre_ID=GenreShort.objects.get(Genre_ID=genre_id)) for genre_id in genres_id]
    UserGenre.objects.bulk_create(user_genres_types)

    return Response('Update complete')
'''
    ALGORYTMIC SECTION
'''
# THE LAST SECTION TO DO IS CHANGE METHODS ON DB
# CHANEG TABLES
# GET THE DATA FROM REC VIA TRIGGER
@api_view(['GET'])
def getUserDataAlgo(request, id):
    user = BookReaders.objects.get(FireBaseAuth=id)
    numberHistory = History.objects.filter(Reader_ID=user.Reader_ID).count()
    if numberHistory < 4:
        normal_recomendations = OFFTOP_Recomendations.objects.all()
        serializer = OFFTOPSerializer(normal_recomendations,many=True)         
    else:
        user_recomendation = AlgorithmRecomendations.objects.filter(Reader_ID=user.Reader_ID)
        print(user_recomendation)
        if len(user_recomendation) < 1:
             normal_recomendations = OFFTOP_Recomendations.objects.all()
             serializer = OFFTOPSerializer(normal_recomendations,many=True) 
        else:
            serializer = AlogrithmSerializer(user_recomendation,many=True) 

    return Response(serializer.data)

'''
    REVIEW SECTION
'''

@api_view(['POST'])
def addReview(request):
    data_user = request.data
    print(data_user)
    user = data_user['uid']
    book = data_user['book_id']
    rating = data_user['review']

    user_obj = BookReaders.objects.get(FireBaseAuth=user)
    book_obj = Book.objects.get(Book_ID=book)
    review_counter = Review.objects.filter(Reader_ID=user_obj, Book_ID = book_obj).values_list('Review',flat=True)

    if len(review_counter) == 0:
        print("ADDING NEW REVIEW")
        Review.objects.create(
        Review = rating,
        Reader_ID = user_obj,
        Book_ID = book_obj,
        )

        book_obj.Rating = round((book_obj.Rating*book_obj.NumberReviews +rating) /(book_obj.NumberReviews +1), 2)
        book_obj.NumberReviews = book_obj.NumberReviews +1
        book_obj.save()

        return Response("Added new opinion")
        
    else:
        print("MODIFY")
        print(review_counter)
        Review.objects.filter(Reader_ID=user_obj, Book_ID = book_obj).update(Review=rating)
        book_obj.Rating = round((book_obj.Rating*book_obj.NumberReviews - review_counter[0] + rating) /(book_obj.NumberReviews), 2)
        book_obj.save()
        return Response("Modify existing opition")
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book, BookReaders, History
from .serializer import BookSerializer, BookReadersSerializer
# Create your views here.



@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/books/',
        '/api/books/<id>/reviews/',
        '/api/history/<uid>/',
    ]
    return Response(routes)


@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(Book_ID=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)    

@api_view(['GET'])
def getUser(request, id):
    user = BookReaders.objects.get(FireBaseAuth=id)
    serializer = BookReadersSerializer(user, many=False)
    print(serializer.data)
    return Response(serializer.data)    


@api_view(['PUT'])
def updateUser(request, id):

    user = BookReaders.objects.get(FireBaseAuth=id)
    serializer = BookReadersSerializer(user, many=False)

    data_user = request.data
    
    user.Name = data_user['name'],
    user.Age = data_user['age'],
    user.Sex = data_user['sex'],
    print(serializer.data)
    ## HERE DB NOT RESPONDING
    return Response(serializer.data)

@api_view(['POST'])
def registerUser(request):
    data_user = request.data
    new_user = BookReaders.objects.create(
        Name = data_user['name'],
        FireBaseAuth = data_user['uid'],
        Age = data_user['age'],
        Sex = data_user['sex'],
    )
    serializer = BookReadersSerializer(new_user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getUserHistory(request, user_auth_key):
    user = History.objects.get(Reader_ID=user_auth_key)
    serializer = BookReadersSerializer(user, many=False)
    return Response(serializer.data)    
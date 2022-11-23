from pickle import FALSE
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserReview
from .serializer import UserReviewSerializer


@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/books/',
        '/api/books/<id>/reviews/',
        '/api/history/<uid>/',
    ]
    return Response(routes)
    
@api_view(['POST'])
def NewReview(request):
    
    data_user = request.data
    print(data_user)
    new_user = UserReview.objects.create(
        Review = data_user['review'],
        Books = data_user['books'],
    )
    serializer_user = UserReviewSerializer(new_user, many=False)
    return Response(serializer_user.data)

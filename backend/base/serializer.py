from rest_framework import serializers
from .models import BookReaders, Book, Genre, History, UserGenre, AlgorithmRecomendations

class BookReadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReaders
        fields = '__all__'

class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGenre
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['Genre_Name']

class HistorySerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='Book_ID.Name', read_only=True)
    Auhtor_Name = serializers.CharField(source='Book_ID.Author.Author_Name', read_only=True)
    Book_Image =  serializers.CharField(source='Book_ID.ImgSource', read_only=True)
    class Meta:
        model = History
        fields = ['AllRenatls_ID','Reader_ID','Date_Taken','Book_ID','Returned','Name','Auhtor_Name','Book_Image']



class AlogrithmSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='Book_ID.Name', read_only=True)
    Auhtor_Name = serializers.CharField(source='Book_ID.Author.Author_Name', read_only=True)
    Book_Image =  serializers.CharField(source='Book_ID.ImgSource', read_only=True)
    class Meta:
        model = AlgorithmRecomendations
        fields = ['Alogritm_ID','Reader_ID','Book_ID','Name','Auhtor_Name','Book_Image']

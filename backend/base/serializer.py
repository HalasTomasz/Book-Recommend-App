from rest_framework import serializers
from .models import BookReaders, Book, Genre, History, UserGenre, AlgorithmRecomendations, BookGenres, Review, GenreShort 

class BookReadersSerializer(serializers.ModelSerializer):
    Usergenre =  serializers.SerializerMethodField() 
    class Meta:
        model = BookReaders
        fields = '__all__'

    def get_Usergenre(self, obj):
        genres_id = UserGenre.objects.filter(Reader_ID=obj.Reader_ID).values_list('Genre_ID',flat=True)
        genres_name =  GenreShort.objects.filter(Genre_ID__in=genres_id)
        serializer = GenreSerializer(genres_name, many=True)
        return serializer.data
        
class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGenre
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):

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

class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenres
        fields = ['Genre_Name']

class BookSerializer(serializers.ModelSerializer):
   
    Auhtor_Name = serializers.CharField(source='Author.Author_Name', read_only=True)
    BookGenre =  serializers.SerializerMethodField() 
    #serializers.ListSerializer(source='Book_ID.Genre_ID.Genre_Name' , child=serializers.CharField())
    # HERE ADD TP READ USER REVIEW 
    class Meta:
        model = Book
        fields = ['Book_ID','Name','Description','Rating','Availability', 'NumberReviews','ImgSource','Auhtor_Name','BookGenre']

    def get_BookGenre(self, obj):
        genre_id = BookGenres.objects.filter(
            Book_ID=obj.Book_ID).values_list('Genre_ID',flat=True)
        selected_genres = Genre.objects.filter(Genre_ID__in=genre_id)
        return  GenreSerializer(selected_genres, many=True).data


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
        fields = ['Alogritm_ID','Book_ID','Name','Auhtor_Name','Book_Image']

class OFFTOPSerializer(serializers.ModelSerializer):
    Name = serializers.CharField(source='Book_ID.Name', read_only=True)
    Auhtor_Name = serializers.CharField(source='Book_ID.Author.Author_Name', read_only=True)
    Book_Image =  serializers.CharField(source='Book_ID.ImgSource', read_only=True)
    class Meta:
        model = AlgorithmRecomendations
        fields = ['Alogritm_ID','Book_ID','Name','Auhtor_Name','Book_Image']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['Review']
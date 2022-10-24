from rest_framework import serializers
from .models import BookReaders, Book, History


class BookReadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReaders
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
from rest_framework import serializers

from books.models import Author, Book

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        field = '__all__'


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = AuthorSerializers(instance.author).data   
        return response
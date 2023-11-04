from django.shortcuts import get_object_or_404

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from books.models import Book, Author

from books.serializers import AuthorSerializers
from books.serializers import BookSerializers


class RetrieveBooks(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        books_list = Book.objects.all().values()
        return Response(books_list, status=status.HTTP_200_OK)

class RetrieveAuthors(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        author_list = Author.objects.all()
        serializer = AuthorSerializers(author_list, many = True)
        return Response(serializer.data)

class CreateAuthor(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        author_obj = Author.objects.create(
            first_name=request.data.get('nombre', ''),
            last_name=request.data.get('apellido', ''),
            birth_day=request.data.get('fecha nacimiento', '')  
        )
        return Response({'message': 'Autor creado exitosamente'}, status=status.HTTP_201_CREATED)

class CreateBook(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        book_obj = Book.objects.create(
            name=request.data.get('nombre', ''),
            isbn=request.data.get('isbn', 0),
            publisher_date=request.data.get('fecha publicacion', '1700-01-01'),
            author_id=request.data.get('autor_id', 1)  
        )
        return Response({'message': 'Libro creado exitosamente'}, status=status.HTTP_201_CREATED)
    

class RetrieveAuthorAPIView(APIView):
    permission_classes = (AllowAny)

    def get(self, request, author_id):
        author_obj = Author.objects_or_404(Book, pk=author_id)
        serializer = AuthorSerializers(author_obj)
        return Response(serializer.data)
    
    def put(sel, request, author_id):
        author_obj = Author.objects_or_404(Book, pk=author_id)
        serializer = AuthorSerializers(instance=author_obj, data=request.data, partial=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delte(self, request, author_id):
        author_obj = Author.objects_or_404(Book, pk=author_id)
        author_obj.status = False
        author_obj.save()
        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)


    

class RetrieveBooksAPIView(APIView):
    permission_classes = (AllowAny)

    def get(self, request, book_id):
        books_obj = Book.objects_or_404(Book, pk=book_id)
        serializer = BookSerializers(books_obj)
        return Response(serializer.data)
    
   
    


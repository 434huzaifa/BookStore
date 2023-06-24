from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BookSerializer
from .models import Book
# Create your views here.
@api_view(['GET'])
def overview(request):
    urls={
        'book_list':'book-list/',
        'book_details':'book-details/<str:pk>/',
        'create_book':'create-book/',
        'update_book':'update-book/<str:pk>/',
        'delete_book':'delete-book/<str:pk>/'
    }
    return Response(urls)

@api_view(['GET'])
def book_list(request):
    books=Book.objects.all()
    serializer=BookSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_details(request,pk):
    book=Book.objects.get(id=pk)
    serializer=BookSerializer(book,many=False)
    return Response(serializer.data)

@api_view(['post'])
def create_book(request):
   
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(request.data)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def update_book(request,pk):
    book=Book.objects.get(id=pk)
    serializer=BookSerializer(instance=book,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def delete_book(request,pk):
    book=Book.objects.get(id=pk)
    book.delete()
    return Response("Delete Successfull")
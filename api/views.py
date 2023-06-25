from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .serializer import BookSerializer
from .models import Book
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
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
def admin_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user != None:
        login(request, user)
        return Response("authentication success",status=200)
    return Response("authentication faild",status=401)

@api_view(['post'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_book(request):
   
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(request.data)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def admin_logout(request):
    logout(request) 
    return Response("Logout Finish")


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
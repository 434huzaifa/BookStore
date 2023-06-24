from django.shortcuts import  render, redirect

# Create your views here.

def book_list(request):
    return render(request,'book_list.html')

def book_details(request,pk):
    return render(request,'book_details.html',context={'pk':pk})

def cart(request):
    return render(request,'cart.html')

def create_book(request):
    return render(request,'create_book.html')
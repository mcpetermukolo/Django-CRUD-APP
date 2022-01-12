from django.shortcuts import render, redirect
from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'crud_django/index.html', context)

def create(request):
    books = Book(Title=request.POST['Title'], Author=request.POST['Author'],Subject=request.POST['Subject'])
    books.save()
    return redirect('/')

def edit(request, id):
    books = Book.objects.get(id=id)
    context = {'books': books}
    return render(request, 'crud_django/edit.html', context)

def update(request, id):
    book = Book.objects.get(id=id)
    book.Title = request.POST['Title']
    book.Author = request.POST['Author']
    book.Subject = request.POST['Subject']
    book.save()
    return redirect('/crud_django/')

def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/crud_django/')
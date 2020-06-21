from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from django.apps import apps
User = apps.get_model('login', 'User')

def index(request):
    user = User.objects.get(id=request.session['userid'])
    all_books = Book.objects.all().order_by('-created_at')

    context = {
        'user':user,
        'all_books':all_books,
    }
    return render(request, 'books/index.html', context)

def adding_a_book(request):
    errors = Book.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        user = User.objects.get(id=request.session['userid'])
        added_book = Book.objects.create(title=request.POST['title'], description=request.POST['description'], uploaded_by = user)

        added_book.users_who_like.add(user) #whoever uploaded the book automatically likes it

        return redirect('/books')

def display_book(request, id):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=id)

    context = {
        'book': book,
        'user':user,
    }
    return render(request,'books/display_edit.html', context)
    
def edit_and_save(request, id):
    user = User.objects.get(id=request.session['userid'])
    edit_book = Book.objects.get(id = id)

    errors = Book.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect(f'/books/{edit_book.id}')
    else:
        edit_book.title = request.POST['title']
        edit_book.description = request.POST['description']
        edit_book.save()   
        return redirect('/books')

def delete_book(request, id):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=id, uploaded_by = user)
    book.delete()
    return redirect('/books')

def favorite(request, id):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=id)

    book.users_who_like.add(user)

    return redirect('/books')

def unfavorite(request, id):
    user = User.objects.get(id=request.session['userid'])
    book = Book.objects.get(id=id)

    book.users_who_like.remove(user)

    return redirect(f'/books/{id}')



    

# Create your views here.

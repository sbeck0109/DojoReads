from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from loginReg_app.models import User
from DojoReads_app.models import Book, Review, Author
import bcrypt


def index(request):
  if "user_id" not in request.session:
    return redirect('/')
  this_user = User.objects.get(id=request.session['user_id'])
  all_books = Book.objects.all()
  all_authors = Author.objects.all()
  all_reviews = Review.objects.all()
  all_users = User.objects.all()
  all_books_reversed=Book.objects.all().order_by('-id')
  last_book = all_books_reversed[0]
  second_last_book = all_books_reversed[1]
  third_last_book = all_books_reversed[2]
  last_3_books = [all_books_reversed[0], all_books_reversed[1], all_books_reversed[2] ]
  context = {
    "this_user" : this_user,
    "all_books" : all_books,
    "all_authors" : all_authors,
    "all_reviews" : all_reviews,
    "all_books_reversed" : all_books_reversed,
    "last_book" : last_book,
    "second_last_book" : second_last_book,
    "third_last_book" : third_last_book,
    "last_3_books" : last_3_books
  }
  return render(request, 'index.html', context)

def add(request):
  if "user_id" not in request.session:
    return redirect('/')
  user_id = request.session['user_id']
  this_user = User.objects.get(id = user_id)
  all_books = Book.objects.all()
  all_authors = Author.objects.all()
  context = {
    "all_books" : all_books,
    "all_authors" : all_authors,
    "this_user" : this_user,
  }
  return render(request, "add.html", context)

def add_post(request):
  if "user_id" not in request.session:
    return redirect('/')
  errors = Book.objects.book_validator(request.POST)
  if len(errors):
    for key, value in errors.items():
      messages.error(request, value)
    return redirect("/books/add_book_and_review")
  else:
    user_id = request.session['user_id']
    this_user = User.objects.get(id = user_id)
    print(this_user)
    book_title = request.POST['title']
    book_review = request.POST['review']
    book_rating = request.POST['rating']
    if request.POST['new_author']:
      book_author = Author.objects.create(name=request.POST['new_author'])
    else:
      book_author = Author.objects.create(name=request.POST['author'])
    new_book = Book.objects.create(title = book_title, author = book_author)
    new_review = Review.objects.create(review=book_review, rating = book_rating, reviewed_by = this_user, about_title = new_book)
    new_book.save()
    print("***********************", book_title)
    return redirect(f'/books/{new_book.id}')
def details(request, book_id):
  if "user_id" not in request.session:
      return redirect('/')
  user_id = request.session['user_id']
  this_user = User.objects.get(id = user_id)
  this_book = Book.objects.get(id = book_id)

  context = {
      "this_book" : this_book,
      "this_user" : this_user

  }
  print('logged in user is:', this_user)
  return render(request, "details.html", context)
def delete_book(request, book_id):
  if "user_id" not in request.session:
      return redirect('/')
  this_book = Book.objects.get(id = book_id)
  this_book.delete()
  return redirect('/books')

def post_review(request, book_id):
  if "user_id" not in request.session:
      return redirect('/')
  user_id = request.session['user_id']
  this_user = User.objects.get(id = user_id)
  this_book = Book.objects.get(id = book_id)
  review = request.POST['review']
  rating = request.POST['rating']
  new_review = Review.objects.create(review = review, rating = rating, reviewed_by = this_user, about_title = this_book)
  new_review.save()
  return redirect(f'/books/{this_book.id}')

def delete_review(request, review_id):
  if "user_id" not in request.session:
      return redirect('/')
  this_review = Review.objects.get(id = review_id)
  this_book = this_review.about_title
  this_review.delete()
  return redirect(f'/books/{this_book.id}')

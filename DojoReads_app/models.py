from django.db import models
from loginReg_app.models import User

class BookManager(models.Manager):
  def book_validator(self, postData):
    errors = {}
    if len(postData['title']) < 1:
      errors['title'] = "Title required!"
    return errors
class AuthorManager(models.Manager):
  def author_validator(self, postData):
    errors = {}
    if len(postData['name']) < 1:
      errors['name'] = "Name required!"
    return errors
class ReviewManager(models.Manager):
  def review_validator(self, postData):
    errors = {}
    if len(postData['review']) < 1:
      errors['name'] = "Please leave a review!"
    if (postData['rating']) < 1:
      errors['rating'] = "Please rate this book"
    return errors
class Author(models.Model):
  name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
  title = models.CharField(max_length=255)
  author = models.ForeignKey(Author, related_name="book", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = BookManager()
class Review(models.Model):
  rating = models.IntegerField()
  review = models.CharField(max_length=255)
  reviewed_by = models.ForeignKey(User, related_name="book_reviewed", on_delete=models.CASCADE)
  about_title = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ReviewManager()

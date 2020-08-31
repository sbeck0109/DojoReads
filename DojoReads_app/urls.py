from django.urls import path
from . import views

app_name = "DojoReads"
urlpatterns = [
    path('', views.index, name="my_index"),
    path('/add_book_and_review', views.add, name="my_add_book"),
    path('/add_book_and_review/post', views.add_post, name="my_add_post_book"),
    path('/<int:book_id>', views.details, name="my_book_review"),
    path('/<int:book_id>/review', views.post_review, name="my_add_review"),
    path('/<int:book_id>/delete', views.delete_book, name="my_delete_book"),
    path('/<int:review_id>/delete', views.delete_review, name="my_delete_review"),
]

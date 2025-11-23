from django.urls import path
from . import views

urlpatterns = [
    # старые
    path('', views.HomeView.as_view(), name='home'),
    path('hello/<str:name>/', views.hello_world, name='hello-with-name'),
    path('redirect/', views.redirect_example, name='redirect-example'),
    path('json/', views.json_example, name='json-example'),
    path('cookies/', views.show_cookies, name='show-cookies'),

    # CRUD авторов и книг
    path('authors/', views.author_list, name='author-list'),
    path('authors/create/', views.author_create, name='author-create'),
    path('authors/<int:pk>/edit/', views.author_update, name='author-update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author-delete'),
    path('authors/<int:pk>/details/', views.author_details_view, name='author-details'),

    path('books/', views.book_list, name='book-list'),
    path('books/create/', views.book_create, name='book-create'),
    path('books/<int:pk>/edit/', views.book_update, name='book-update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book-delete'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),

    # QuerySet и связи
    path('books/by-author/', views.books_by_author, name='books-by-author'),
    path('books/values/', views.books_values_view, name='books-values'),
    path('books/sets/', views.books_set_operations, name='books-sets'),
    path('books/aggregates/', views.books_aggregates, name='books-aggregates'),
    path('books/sql/', views.raw_sql_example, name='books-sql'),
    path('books/publishers/', views.books_with_publishers, name='books-with-publishers'),
    path('books/genres/', views.books_with_genres, name='books-with-genres'),
]

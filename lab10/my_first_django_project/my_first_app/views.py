from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import TemplateView
from django.db.models import Count, Avg, Max, Min
from django.db import connection

from .models import Author, Book, Publisher, Genre, AuthorDetails
from .forms import AuthorForm, BookForm, AuthorDetailsForm
from django.db.models.functions import Cast
from django.db.models import DateTimeField



class HomeView(TemplateView):
    template_name = "home.html"

def hello_world(request, name="World"):
    age = request.GET.get("age")

    names = ["Alex", "Masha", "Kate"]

    context = {
        "current_name": name,
        "age": age,
        "names": names,
    }

    response = render(request, "base.html", context)

    response.set_cookie("username", name)

    return response


def redirect_example(request):
    response = redirect('hello-with-name', name='Guest')
    response.status_code = 302
    return response


def json_example(request):
    user_data = {
        "name": "Sanya",
        "age": 20,
        "status": "student",
    }
    return JsonResponse(user_data)


def show_cookies(request):
    cookies = request.COOKIES

    if not cookies:
        return HttpResponse("<h1>No cookies found</h1>")

    lines = []
    for key, value in cookies.items():
        lines.append(f"{key}: {value}")

    html = "<br>".join(lines)
    return HttpResponse(html)


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


def book_list(request):
    books = Book.objects.select_related('author', 'publisher').prefetch_related('genres')
    return render(request, 'book_list.html', {'books': books})


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')
        else:
            print(form.errors)  # <<< добавь
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form, 'action': 'Создание автора'})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form, 'action': 'Создание книги'})


def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author_form.html', {'form': form, 'action': 'Редактирование автора'})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form, 'action': 'Редактирование книги'})


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author-list')
    return render(request, 'confirm_delete.html', {'object': author, 'type': 'автора'})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'confirm_delete.html', {'object': book, 'type': 'книгу'})


def books_by_author(request):
    author_id = request.GET.get('author_id')
    author = None
    books = Book.objects.all()

    if author_id:
        books = books.filter(author_id=author_id)
        author = Author.objects.filter(id=author_id).first()

    context = {
        'books': books,
        'author': author,
        'authors': Author.objects.all(),  # чтобы можно было выбрать автора из списка
    }
    return render(request, 'books_by_author.html', context)


def books_values_view(request):
    # список книг в виде словарей
    books_values = Book.objects.values('id', 'title', 'publication_date').order_by('publication_date')

    # список только названий
    titles_list = Book.objects.values_list('title', flat=True).order_by('title')

    context = {
        'books_values': books_values,
        'titles_list': titles_list,
    }
    return render(request, 'books_values.html', context)


def books_set_operations(request):
    # книги до 2020
    qs_old = Book.objects.filter(publication_date__lt='2020-01-01')
    # книги после 2015
    qs_new = Book.objects.filter(publication_date__gt='2015-01-01')

    union_qs = qs_old.union(qs_new)
    intersection_qs = qs_old.intersection(qs_new)
    difference_qs = qs_old.difference(qs_new)

    context = {
        'qs_old': qs_old,
        'qs_new': qs_new,
        'union_qs': union_qs,
        'intersection_qs': intersection_qs,
        'difference_qs': difference_qs,
    }
    return render(request, 'books_sets.html', context)


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Книга не найдена")

    return render(request, 'book_detail.html', {'book': book})


def books_aggregates(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        max_date=Max('publication_date'),
        min_date=Min('publication_date'),
        avg_year=Avg('publication_date__year'),  # средний год публикации
    )

    return render(request, 'books_aggregates.html', {'stats': stats})

def books_with_publishers(request):
    books = Book.objects.select_related('publisher').all()
    return render(request, 'books_with_publishers.html', {'books': books})


def books_with_genres(request):
    books = Book.objects.prefetch_related('genres').all()
    return render(request, 'books_with_genres.html', {'books': books})


def author_details_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    details = getattr(author, 'details', None)  # через related_name='details'

    return render(request, 'author_details.html', {
        'author': author,
        'details': details,
    })


def raw_sql_example(request):
    # Пример простого SQL-запроса: посчитать количество книг
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM my_first_app_book;")
        row = cursor.fetchone()

    total_books = row[0] if row else 0
    return HttpResponse(f"Всего книг (через RAW SQL): {total_books}")
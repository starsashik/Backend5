# Содержит data-классы согласно шагу 8.

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    isbn: str

@dataclass
class Author:
    name: str
    birth_year: int
    nationality: str


@dataclass
class LibraryMember:
    name: str
    member_id: str
    borrowed_books: list = None  # Список объектов Book

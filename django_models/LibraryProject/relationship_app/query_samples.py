# relationship_app/query_samples.py

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'.")

def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library.name} Library:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library.name} Library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}' library.")

if __name__ == "__main__":
    # Sample data queries
    print("=== Query All Books by a Specific Author ===")
    query_all_books_by_author("J.K. Rowling")
    print("\n=== List All Books in a Library ===")
    list_all_books_in_library("Central Library")
    print("\n=== Retrieve the Librarian for a Library ===")
    retrieve_librarian_for_library("Central Library")

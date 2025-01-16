# views.py
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter, BookFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
import django_filters
from django_filters import rest_framework

class BookListView(generics.ListCreateAPIView):
    """
    GET: Retrieve all books, with optional filtering, searching, and ordering.
    POST: Create a new book (requires authentication).

    Query Parameters:
    - title: Filter by book title (partial match).
    - author: Filter by author name (partial match).
    - publication_year: Filter by publication year (exact match).
    - search: Search by title or author (partial match).
    - ordering: Order by field, e.g., 'title' or 'publication_year'. Prefix with '-' for descending order.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # Allow any user to access the list of books

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # Allow any user to access the list of books

    # Add filtering, search, and ordering support
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']  # Fields that can be used to order results
    ordering = ['title'] 
    "DetailView", "CreateView", "UpdateView", "DeleteView"

    "from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated", "IsAuthenticated"

    "filters.OrderingFilter"
    "filters.SearchFilter"
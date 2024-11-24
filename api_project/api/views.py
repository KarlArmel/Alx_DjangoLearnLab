from django.shortcuts import render
["generics.ListAPIView"]
["viewsets.ModelViewSet"]
# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookViewSet(ModelViewSet):
    """
    A viewset that provides the standard CRUD operations for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
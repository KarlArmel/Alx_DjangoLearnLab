# relationship_app/views.py
from django.shortcuts import render,redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
["relationship_app/register.html"]

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to a home or dashboard view after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
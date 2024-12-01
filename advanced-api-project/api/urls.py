from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from . import views

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
     path('', include(router.urls)),
     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
     path('books/', views.BookListView.as_view(), name='book-list'),  # ListView and CreateView
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # DetailView
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),  # CreateView
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),  # UpdateView
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # DeleteView

]


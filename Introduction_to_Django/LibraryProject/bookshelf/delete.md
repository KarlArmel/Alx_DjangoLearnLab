## Delete Operation

**Command**:
```python
# Delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four", author="George Orwell")
book.delete()

# Try retrieving all books (should return an empty queryset if the deletion was successful)
books = Book.objects.all()
print(books)

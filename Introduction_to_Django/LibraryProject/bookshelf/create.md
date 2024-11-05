## Create Operation

**Command**:

```python
from yourapp.models import Book

# Creating a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output the book to confirm creation
print(book)

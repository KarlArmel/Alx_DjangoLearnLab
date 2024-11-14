## Update Operation

**Command**:
```python
# Retrieve the book
book = Book.objects.get(title="1984", author="George Orwell")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Output the updated book
print(book)

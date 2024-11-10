## Retrieve Operation

**Command**:
```python
# Retrieve the created book
book = Book.objects.get(title="1984", author="George Orwell")

# Output the details of the book
print(book)

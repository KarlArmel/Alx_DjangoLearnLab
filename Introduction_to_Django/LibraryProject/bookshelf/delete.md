## Delete Operation
from bookshelf.models import Book


In this operation, we will delete the `Book` instance that we created earlier and confirm its deletion by attempting to retrieve it again.

### Command to execute in Django shell:

First, open the Django shell with:

```bash
python manage.py shell
book.delete

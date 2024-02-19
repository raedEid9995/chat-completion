---
title: Untitled doc
---
<SwmSnippet path="/library.py" line="1">

---

This code defines a `Book` class that represents a book. Each book has a `title`, `author`, and an `is_available` attribute. The `is_available` attribute indicates whether the book is currently available or not.

The class has three methods:

- `__init__`: This is the constructor method that initializes a `Book` object with a `title` and an `author`. It also sets the `is_available` attribute to `True`.
- `borrow_book`: This method allows someone to borrow the book. If the book is currently available (`is_available` is `True`), it sets `is_available` to `False` and returns `True`. If the book is already borrowed (`is_available` is `False`), it returns `False`.
- `return_book`: This method allows someone to return the book. It sets `is_available` to `True`, indicating that the book is now available for borrowing again.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        self.is_available = True

```

---

</SwmSnippet>

<SwmSnippet path="/library.py" line="18">

---

This code defines a class with an `__init__` method that takes a `name` parameter. The `name` parameter is then assigned to an instance variable also called `name`. Additionally, an empty list called `borrowed_books` is created as an instance variable.

```python
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

```

---

</SwmSnippet>

```mermaid
graph TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]
```

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBY2hhdC1jb21wbGV0aW9uJTNBJTNBcmFlZEVpZDk5OTU=" repo-name="chat-completion"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>

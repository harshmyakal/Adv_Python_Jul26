class book:
    def __init__(self, title, author, pages=0):  # Added a default value for pages
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"
        
    def __repr__(self):
        return f"book('{self.title}', '{self.author}')"
        
    def __eq__(self, other):
        if not isinstance(other, book):
            return False
        return self.title == other.title and self.author == other.author

# Unindented these lines to run outside the class definition
book1 = book("Python 101", "Mark Davis")
book2 = book("Python 101", "Mark Davis")
book3 = book("Python 201", "John Smith")

print(repr(book1))
print(book1 == book2)  # True   
print(book1 == book3)  # False
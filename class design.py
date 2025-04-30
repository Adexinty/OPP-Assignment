# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")


# Subclass with polymorphism (method override)
class SpecialBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)

    def display_info(self):  # Overridden method = Polymorphism
        print(f"[Special Edition] Title: {self.title}, Author: {self.author}")


# Create instances
book1 = Book("Think and Grow Rich", "Napoleon Hill")
book2 = Book("How to Talk to Anyone", "Leil Lowndes")
special = SpecialBook("Think and Grow Rich", "Napoleon Hill")

# Call methods
book1.display_info()
book2.display_info()
special.display_info()

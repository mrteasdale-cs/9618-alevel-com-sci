#Part 1: Define the Class
class Book:
    def __init__(self, title, author, isbn):
        self.__title = title #private string
        self.__author = author #private string
        self.__isbn = isbn #private int

    # Part 2: Add Public Methods
    def display_details(self):
        print("Type: Book")
        print(f"Title: {self.__title} Author: {self.__author} ISBN: {self.__isbn}")


#Part 3: Create Objects and Test Methods
book1 = Book("CS with M", "Myran", "12345")
book1.display_details()

class Ebook(Book):
    def __init__(self, title, author, isbn, filesize):
        super().__init__(title, author, isbn)
        self.__filesize = filesize

    # Part 4: Add a Derived Class
    def display_ebook_details(self):
        super().display_details()
        print(f"File Size: {self.__filesize} MB")

#Part 5: Polymorphism
# method is overridden
# person1.speak() --> "hi"
# person2.speak() --> "hello"
    def display_details(self):
        print("Type: Ebook")
        print("Title:", self._Book__title)
        print("Author:", self._Book__author)
        print("ISBN:", self._Book__isbn)
        print("Filesize:", self.__filesize)

ebook1 = Ebook("CS with M - EBOOK", "Myran", "12345", 500)
ebook1.display_details()
ebook1.display_ebook_details()
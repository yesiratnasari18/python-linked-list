class Book:
    def __init__(self, title):
        self.title = title
        self.next = None

class Visitor:
    def __init__(self, name):
        self.name = name
        self.books = None

    def borrow_book(self, title):
        new_book = Book(title)

        if self.books is None:
            self.books = new_book
        else:
            current = self.books
            while current.next is not None:
                current = current.next
            current.next = new_book

    def print_borrowed_books(self):
        if self.books is None:
            print(f"{self.name} Belum meminjam buku.")
        else:
            print(f"Buku yang dipinjam oleh {self.name}:")
            current = self.books
            while current is not None:
                print(current.title)
                current = current.next


visitors = []

visitor1 = Visitor("Yesi")
visitor1.borrow_book("Harry Potter")
visitor1.borrow_book("To Kill a Mockingbird")
visitors.append(visitor1)

visitor2 = Visitor("Ratna")
visitor2.borrow_book("Peterpan")
visitors.append(visitor2)

visitor3 = Visitor("Sari")
visitor3.borrow_book("Ivanna Van Djik")
visitor3.borrow_book("Danur")
visitor3.borrow_book("Maddah")
visitors.append(visitor3)

for visitor in visitors:
    visitor.print_borrowed_books()



class Book:
    def __init__(self, name, book_type):
        self.name = name
        self.book_type = book_type

    def print_book_info(self):
        print(f'Book Info: {self.name} - {self.book_type}')

    @classmethod
    def create_regular_book(cls, name):
        return cls(name, 'Regular book')

    @staticmethod
    def representer(name):
        print(name)


# book = Book('Test', 'Regular Book')
book = Book.create_regular_book('Test')
book.print_book_info()
Book.representer()

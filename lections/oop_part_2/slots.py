class Book:
    # __slots__ = ('name', 'book_type')

    def __init__(self, name):
        self.name = name

book = Book('Test')
print(book.name)

book.name = 'Test1'
print(book.name)

book.book_type = 'Regular Book'
print(book.book_type)

# book.author = 'Test Author'
# print(book.author)

print(book.__slots__)
# print(book.__dict__)


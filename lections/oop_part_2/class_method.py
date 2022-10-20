# class MyClass:
#     TOTAL_OBJECTS = 0
#
#     def __init__(self):
#         self.my_object = 'hello'
#         MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1
#
#     @classmethod
#     def my_method(cls):
#         print('hi')
#
#     @classmethod
#     def total_objects(cls):
#         print(f'Total object: {cls.TOTAL_OBJECTS}')
#
#
# my_class = MyClass()
# my_class_1 = MyClass()
# my_class_2 = MyClass()
# # print(my_class.my_object)
# #
# # my_class.my_method()
#
# MyClass.total_objects()

class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)

book = Book('Test', 'hardcover', '300')
print(book.name)
print(book.book_type)
print(book.weight)

hardcover_book = Book.hardcover('Test_1', 200)
print(hardcover_book.name)
print(hardcover_book.book_type)
print(hardcover_book.weight)

paperback_book = Book.paperback('Test_1', 200)
print(paperback_book.name)
print(paperback_book.book_type)
print(paperback_book.weight)
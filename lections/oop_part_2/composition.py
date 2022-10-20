class Book:
    def __init__(self):
        page_1 = Page('This is content of page 1')
        page_2 = Page('This is content of page 2')
        page_3 = Page('This is content of page 3')
        self.book = [page_1.content, page_2.content, page_3.content]

class Page:
    def __init__(self, content):
        self.content = content

book = Book()
print(book.book)
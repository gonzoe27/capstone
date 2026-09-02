class Author:
    def __init__(self, name):
        self.name = name 
        self.books = []

    def publish(self, title):
        if title.lower() in (book.lower() for book in self.books):
            return f'Error: Book "{title}" is already published.'
        else:
            self.books.append(title)
            return f'Book "{title}" published successfully.'

    def __str__(self):
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = 'No Books found'
        #this also works book_list = ', '.join(self.books) or 'No Books found'
        return f'Author: {self.name}  Books Published: {book_list}'

shakespeare = Author('William Shakespeare')
shakespeare.publish('Hamlet')
shakespeare.publish('Richard III')
print(shakespeare.publish('Hamlet')) #test for duplicate book

print(shakespeare)


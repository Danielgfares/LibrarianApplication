from book import Book

class BookShelf():
    name=""
    books = dict()
    
    def __init__(self, name=""):
        self.name = name
        
    def getName(self):
        return self.name
    
    def addBook(self, book):
        self.books[book.getISBN()] = book
        
    def removeBook(self, bookISBN):
        if (bookISBN in books):
            del books[bookISBN]
    
    def getBook(self, ISBN):
        if (ISBN in self.books):
            return self.books[ISBN]
        else:
             raise Exception("Book with ISBN [{}] DONT exists".format(ISBN))

    def getBookByTitle(self, title):
        for key in self.books.keys():
            book = self.books[key]
            if (book.title == title):
                return book
        raise Exception("Book with title [{}] DONT exists".format(title))
    
    def __str__(self):
        return list(self.books.keys()).__str__()
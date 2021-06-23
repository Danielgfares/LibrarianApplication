from bookshelf import BookShelf

class Row():
    name = ""
    bookshelfs = dict()
    
    def __init__(self, name=""):
        self.name = name
    
    def getName(self):
        return self.name
    
    def addBookShelf(self, bookShelf):
        self.bookshelfs[bookShelf.getName()] = bookShelf
        
    def removeBookShelf(self, bookShelfName):
        if (bookShelfName in bookshelfs):
            del bookshelfs[bookShelfName]
    
    def getBookShelf(self, bookShelfName):
        if (bookShelfName in self.bookshelfs):
            return self.bookshelfs[bookShelfName]
        else:
            bookshelf = BookShelf(bookShelfName)
            self.bookshelfs[bookShelfName] = bookshelf
            return bookshelf
    
    def __str__(self):
        return list(self.bookshelfs.keys()).__str__() 
    
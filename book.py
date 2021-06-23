import dateutil.parser

class Book():
    title = ""
    auther = ""
    publisher = ""
    publicationYear = 0 
    ISBN = ""
    nPages = 0
    
    def __init__(self, title, auther="unknows", publisher="unknows", publicationYear=dateutil.parser.parse("0001-01-01"), ISBN="unknows", nPages=0):
        self.title = title
        self.auther = auther
        self.publisher = publisher
        self.publicationYear = publicationYear 
        self.ISBN = ISBN
        self.nPages = nPages
        
    def getISBN(self):
        return self.ISBN
    
    def __str__(self):
        return  "Book: \n" +\
                "Title: " + self.title + "\n" +\
                "Auther: " + self.auther + "\n" +\
                "Publisher: " + self.publisher + "\n" +\
                "Publication Year: " + self.publicationYear.isoformat() + "\n" +\
                "ISBN: " + self.ISBN + "\n" +\
                "Number of pages: " + str(self.nPages) + "\n" 
        
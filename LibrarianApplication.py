import pandas as pd
import numpy as np
from os.path import join as path, dirname
from library import Library
from room import Room
from row import Row
from bookshelf import BookShelf
from book import *
df_books = pd.read_excel(path('data', 'BooksDB.xlsx'), index_col='idBook')

def n_books(df):
    '''
    return all books in the data base
    '''
    return df.shape[0]

def get_rooms(df):
    '''
    return all rooms in the data base
    '''
    return df['roomNumber'].drop_duplicates().values

def n_rooms(df):
    '''
    return number of rooms in the data base
    '''
    return df['roomNumber'].drop_duplicates().shape[0]

def get_rows(df):
    '''
    return all rows in the data base
    '''
    return df['rowNumber'].drop_duplicates().values

def n_rows(df):
    '''
    return number of rows in the data base
    '''
    return df['rowNumber'].drop_duplicates().shape[0]

def get_bookshelfs(df):
    '''
    return all bookshelf in the data base
    '''
    return df['bookShelfNumber'].drop_duplicates().values

def n_bookshelf(df):
    '''
    return number of bookshelf in the data base
    '''
    return df['bookShelfNumber'].drop_duplicates().shape[0]

def n_book_rooms(df):
    '''
    return number of books per room in the data base
    '''
    res = pd.crosstab(df['roomNumber'], df['title'])
    return res.sum(axis='columns')

def n_books_rows(df):
    '''
    return number of books per row in the data base
    '''
    res = pd.crosstab(df['rowNumber'], df['title'])
    return res.sum(axis='columns')

def n_books_bookshelfs(df):
    '''
    return number of books per row in the data base
    '''
    res = pd.crosstab(df['bookShelfNumber'], df['title'])
    return res.sum(axis='columns')

def get_count_rows_per_room(df):
    return pd.crosstab(df['roomNumber'], df['rowNumber'])

def get_count_bookshelf_per_row(df):
    return pd.crosstab(df['rowNumber'], df['bookShelfNumber'])

def get_count_book_per_bookshelf_ISBN(df):
    return pd.crosstab(df['bookShelfNumber'], df['ISBN'])

def get_count_book_per_bookshelf_title(df):
    return pd.crosstab(df['bookShelfNumber'], df['title'])


table_rows_per_room = get_count_rows_per_room(df_books)
table_bookshelf_per_row = get_count_bookshelf_per_row(df_books)
table_book_per_bookshelf_ISBN = get_count_book_per_bookshelf_ISBN(df_books)
table_book_per_bookshelf_title = get_count_book_per_bookshelf_title(df_books)

def get_by_count_table(df, value):
    isshelf = df.loc[:,value] > 0
    value = df.loc[:,value][isshelf]
    return value.keys().array[0]

def get_bookshelf_ISBN(ISBN):
    return get_by_count_table(table_book_per_bookshelf_ISBN, ISBN)

def get_bookshelf_title(title):
    return get_by_count_table(table_book_per_bookshelf_title, title)

def get_row(shelfbookNumber):
    return get_by_count_table(table_bookshelf_per_row, shelfbookNumber)

def get_room(rowNumber):
    return get_by_count_table(table_rows_per_room, rowNumber)


library = Library()
for i in range(n_books(df_books)):
    data = df_books.loc[i+1]
    book = Book(title=data['title'], auther=data['auther'], publisher=data['publisher'], publicationYear=dateutil.parser.parse(data['publicationYear']), ISBN=data['ISBN'], nPages=data['nPages'])
    room = library.getRoom(data['roomNumber'])
    row = room.getRow(data['rowNumber'])
    bookShelf = row.getBookShelf(data['bookShelfNumber'])
    bookShelf.addBook(book)

if __name__ == "__main__":
    ISBN = ""
    while(ISBN != '0'):
        ISBN = input('To search for a book enter ISBN(0 to exit):')
        if (ISBN == '0'):
            print('Bye bye!')
        else:
            try:
                bookshelfName = get_bookshelf_ISBN(ISBN)
                rowName = get_row(bookshelfName)
                roomName = get_room(rowName)

                room = library.getRoom(roomName)
                row = room.getRow(rowName)
                bookshelf = row.getBookShelf(bookshelfName)
                
                try:
                    book = bookshelf.getBook(ISBN)
                    print(book)
                except: 
                    print('An error occured. Book with ISBN does not exist!')
            except:
                print('ISBN not found!')
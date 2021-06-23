from LibrarianApplication import *

if __name__ == "__main__":
    ISBN = '0-4353-0966-8'
    try:
        bookshelfName = get_bookshelf_ISBN(ISBN)
    except:
        print('error occured!')
    assert bookshelfName == '1AA2', 'title incorrect'
    rowName = get_row(bookshelfName)
    assert rowName == 'N101'
    roomName = get_room(rowName)
    assert roomName == '1A'

    room = library.getRoom(roomName)
    row = room.getRow(rowName)
    bookshelf = row.getBookShelf(bookshelfName)

    try:
        book = bookshelf.getBook(ISBN)
    except:
        print('error occured!')
    assert book, 'ISBN is inccorect'
    print('test passed!')
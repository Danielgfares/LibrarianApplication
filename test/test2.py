from LibrarianApplication import *

if __name__ == "__main__":
    title = 'Texts from Denmark'
    try:
        bookshelfName = get_bookshelf_title(title)
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
        book = bookshelf.getBookByTitle(title)
    except:
        print('error occured!')
    assert book, 'book not found'
    print('test passed!')

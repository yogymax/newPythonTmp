

class Book:

    def __init__(self,id,nm,price, authorlist):
        self.bookId = id
        self.bookName = nm
        self.bookPrice = price
        self.bookAuthors = authorlist

    def __str__(self):
        return '{}{}{}{}'.format(self.bookId, self.bookName,self.bookPrice,self.bookAuthors)

    def __repr__(self):
        return str(self)


class Author:

    def __init__(self,id,name):
        self.authorId = id
        self.authorName = name


    def __str__(self):
        return '{}{}'.format(self.authorId, self.authorName)

    def __repr__(self):
        return str(self)


class Library:

    def __init__(self,shelfId,bookList):
        self.libraryShelf = shelfId
        self.libraryBooks = bookList

    def __hash__(self):
        return self.libraryShelf

    def __eq__(self, other):
        return self.libraryShelf == other.libraryShelf

    def __str__(self):
        return '{}{}'.format(self.libraryShelf,self.libraryBooks)

    def __repr__(self):
        return str(self)


if __name__ == '__main__':

    setOfAuthors1 = [Author(1,"Aaa"),Author(2,"Abb"),Author(3,"Acc")]
    setOfAuthors3 = [Author(1, "Aaa"), Author(3, "Acc")]
    setOfAuthors4 = [Author(1, "Aaa"), Author(3, "Acc"), Author(4, "Add")]

    setOfBooks1 = [Book(101,'Python',2043,setOfAuthors1),Book(102,'Java',2203,setOfAuthors3)]
    setOfBooks2 = [Book(103, 'B1', 2603, setOfAuthors1),Book(104,'Angular',9203,setOfAuthors4),Book(105,'B5',203,setOfAuthors3)]
    setOfBooks3 = [Book(103, 'B1', 2603, setOfAuthors1), Book(104, 'Angular', 1231, setOfAuthors1),Book(105, 'B3', 203, setOfAuthors3)]


    LibraryShelfs = {Library(1,setOfBooks1),Library(2,setOfBooks2),Library(3,setOfBooks3)}


    for library in LibraryShelfs:
        for book in library.libraryBooks:
            if book.bookName == 'Angular':
                print(book)

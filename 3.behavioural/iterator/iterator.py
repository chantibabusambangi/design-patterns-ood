from abc import ABC, abstractmethod
#Iterator Interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    @abstractmethod
    def next(self):
        pass

#Aggregate Interface (Collection Interface)
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

#Concrete Collection (BookCollection)
class BookCollection(Aggregate):
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def create_iterator(self):
        return BookIterator(self.books)
    
#Concrete Iterator
class BookIterator(Iterator):
    def __init__(self, books):
        self._books = books
        self._position = 0
    def has_next(self):
        return self._position < len(self._books)

    def next(self):
        if not self.has_next():
            raise StopIteration

        book = self._books[self._position]
        self._position += 1
        return book
    
collection = BookCollection()

collection.add_book("Design Patterns")
collection.add_book("Clean Code")
collection.add_book("Refactoring")

iterator = collection.create_iterator()

while iterator.has_next():
    print(iterator.next())

#The Prototype Design Pattern is a creational design pattern
#  used when the type of objects is to be cloned to produce new objects, especiially creating object from scratch is complex or time taking
# (when needed database queries, network calls needed).

from abc import ABC, abstractmethod
import copy

# Prototype Interface
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete Prototype
class TextBook(Prototype):

    def __init__(self, title, author, chapters):
        self.title = title
        self.author = author
        self.chapters = chapters      # list
        self.student_name = None

    def clone(self):
        return copy.deepcopy(self) # can do manual clone instead of deep copy, either way.
    
    def display(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("Student:", self.student_name)
        print("Chapters:", self.chapters)
        print()

# Create only one master textbook
master_book = TextBook(
    "Operating Systems",
    "Galvin",
    ["Processes", "Threads", "Memory", "File System"]
)

# Clone for Student 1
book1 = master_book.clone()
book1.student_name = "Alice"

# Clone for Student 2
book2 = master_book.clone()
book2.student_name = "Bob"

book1.display()
book2.display()
#If you want to add behavior to an object at runtime(dynamically), 
# unlike inheritance, which adds behavior at compile time, you should use the Decorator Design Pattern.

from abc import ABC, abstractmethod


# ==========================
# Component
# ==========================
class FileSystemNode(ABC):

    @abstractmethod
    def display(self, indent=0):
        pass


# ==========================
# Leaf
# ==========================
class File(FileSystemNode):

    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(" " * indent + f"📄 {self.name}")


# ==========================
# Composite
# ==========================
class Folder(FileSystemNode):

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, node):
        self.children.append(node)

    def remove(self, node):
        self.children.remove(node)

    def display(self, indent=0):
        print(" " * indent + f"📁 {self.name}")

        for child in self.children:
            child.display(indent + 4)
            
root = Folder("Root")

documents = Folder("Documents")
images = Folder("Images")

documents.add(File("resume.pdf"))
documents.add(File("notes.txt"))

images.add(File("photo1.jpg"))
images.add(File("photo2.jpg"))


root.add(documents)
root.add(images)
root.add(File("readme.md"))

root.display()
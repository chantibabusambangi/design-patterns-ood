#Text Editor / Document Editor with Undo Support
#text editor supports : 1.insert text 2.deleet text 3. undo operation

from abc import ABC, abstractmethod

#command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass
    #we can redo as well

#worker
class Document:
    def __init__(self):
        self.text = ""
    def insert(self, new_text):
        self.text += new_text
    def delete(self, count):
        deleted = self.text[-count:]
        self.text = self.text[:-count]
        return deleted
    def show(self):
        print("Document:", self.text)

#concrete commands
class InsertCommand(Command):
    def __init__(self, document, text):
        self.document = document
        self.text = text
    def execute(self):
        self.document.insert(self.text)
    def undo(self):
        self.document.delete(len(self.text))
class DeleteCommand(Command):
    def __init__(self, document, count):
        self.document = document
        self.count = count
        self.deleted_text = ""
    def execute(self):
        self.deleted_text = self.document.delete(self.count)
    def undo(self):
        self.document.insert(self.deleted_text)

#invoker(editor)
class EditorInvoker:
    def __init__(self):
        self.history = []
    def execute_command(self, command):
        command.execute()
        self.history.append(command)
    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("Nothing to undo")

#client code
doc = Document()
editor = EditorInvoker()

cmd1 = InsertCommand(doc, "Hello ")
editor.execute_command(cmd1)
doc.show()

cmd2 = InsertCommand(doc, "World")
editor.execute_command(cmd2)
doc.show()

cmd3 = DeleteCommand(doc, 5)
editor.execute_command(cmd3)
doc.show()

print("Undo last action")
editor.undo()
doc.show()

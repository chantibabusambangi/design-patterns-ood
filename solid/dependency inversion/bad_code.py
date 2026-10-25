#suppose manager class is there with methods addDeveloper, addTester.
class Developer:
    def work(self):
        print("Writing code")
class Tester:
    def work(self):
        print("Testing application")
class Manager:
    def __init__(self):
        self.developers = []
        self.testers = []
    def add_developer(self, developer: Developer):
        self.developers.append(developer)
    def add_tester(self, tester: Tester):
        self.testers.append(tester)
    def manage(self):
        for d in self.developers:d.work()
        for t in self.testers:t.work()

#what wrong is, if a new employee type like designer came
#the manager should know whether the addDesigner method there or not.
#means highlevel module(manager class) depends lowlevel module(addDesigner or addDevloper)
#this violates DIP(dependency inversion principle)

#how to solve create abstractions.
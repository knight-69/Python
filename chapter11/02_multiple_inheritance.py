class Employee:
    company ="ITC"
    def show(self):
        print(f"the name is {self.mame} and the salary is {self.salary}")

class Coder:
    language ="Python"
    def printlanguage(self):
        print(f"Out of all the language here is your language:{self.language}")


class Programmer(Employee,Coder):
    company ="ITC Infotech"
    def ShowLanguage(self):
        print(f"The name is {self.name} and he is a good with {self.language} language")
    
a =Employee()
b=Programmer()

b.show()
b.printlanguage()
b.ShowLanguage()


class Employee:
    # name = "harry"
    language = "py" # This is a class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee()
harry.language ="Javascipt"# This is a Object attribute or aslo known as instance attribute .

harry.greet()
harry.getInfo()

# Employee.getInfo(harry)   #this is same as harry.getInfo as there work is same


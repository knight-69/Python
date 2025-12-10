class Employee:
    # name = "harry"
    language = "py" # This is a class attribute
    salary = 120000

    def __init__(self , name,salary,language): # dunder method which is automatically called
        # print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language =language

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee("harry",130000,"Javascript")
# harry.name = "harry"
print(harry.name,harry.salary,harry.language)
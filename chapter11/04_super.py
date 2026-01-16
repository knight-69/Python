class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# O = Employee()
# print(O.a) # prints the a atttribute 


# O =Programmer()
# print(O.a,O.b)

O =Manager()
print(O.a,O.b,O.c)
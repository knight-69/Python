class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

O = Employee()
print(O.a) # prints the a atttribute 
# print(O.b) # shows an error as the is no b atttribute in a Employee class

O =Programmer()
print(O.a,O.b)

O =Manager()
print(O.a,O.b,O.c)
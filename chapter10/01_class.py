class Employee:
    # name = "harry"
    language = "py" # This is a class attribute
    salary = 120000

harry = Employee()
harry.name ="Harry"# This is a Object attribute or aslo known as instance attribute .
print(harry.name,harry.salary,harry.language)


rohan = Employee()
rohan.name ="Rohan Roro"
print(rohan.name,rohan.salary,rohan.language)

# Here name is instance Attribute and salary and language are class 
# Attribute as they directly belong to the class
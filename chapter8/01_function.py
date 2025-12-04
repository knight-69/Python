# #if i need to do a simple  task like
# a = int(input("Enter Your Number"))
# b = int(input("Enter Your Number"))
# c = int(input("Enter Your Number"))

# average =(a+b+c)/3
# print(average)

# # now if i want to do this task again and again i would do like this

# a = int(input("Enter Your Number"))
# b = int(input("Enter Your Number"))
# c = int(input("Enter Your Number"))

# average =(a+b+c)/3
# print(average)

# a = int(input("Enter Your Number"))
# b = int(input("Enter Your Number"))
# c = int(input("Enter Your Number"))

# average =(a+b+c)/3
# print(average)

# lets say i have to do this again like 5 time i would need to write whole code again and again so there is a simple method like
# we can use anything as for the reference instead of avg like number it does not matter.
# def is called Function Defination.
def avg():
    a = int(input("Enter Your Number"))
    b = int(input("Enter Your Number"))
    c = int(input("Enter Your Number"))

    average =(a+b+c)/3
    print(average)
# after this the code will not print it self multiple time we have to tell it hat how many time it has to run so we the avg() here
avg() #it is called a function call
avg()
avg()
avg()
avg()
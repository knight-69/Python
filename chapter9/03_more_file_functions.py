f= open("file.txt")

# lines = f.readlines()
# print(lines,type(lines))

line1 = f.readline()
print(line1,type(line1))

line2 = f.readline()
print(line2,type(line2))

line3 = f.readline()
print(line3,type(line3))

line4 = f.readline()
print(line4,type(line4))

#so see if there is nothing after the program is done after reading the line that you have and print the program to read when there
# is nothing in the file then then the program will return an empty string.  

# line6 = f.readline()
# print(line6,type(line6))


# line6 = f.readline()
# print(line6 ==)
#The above line will give the output true because the is nothing in that file.
f.close()
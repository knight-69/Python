class demo:
    a =4

o = demo()
print(o.a)# Prints the class attribute because instance attribut is not present
o.a = 0 # Instance attribute is set
print(o.a)# Print the instance attribut because instance attribut is present
print(demo.a)# Prints the class attribute
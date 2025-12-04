a  = 31
t = type (a) # class <int>
print(t)

b = "harry"
t = type (b) # class <str>
print(t)

# what is this is this a float or integer or str
c = "31.2"
t = type (c) 
print(t)

# how we can change the the type by using type function like str into float
c = "31.2"
d = float(c) # c but the type should be float
t = type (d) 
print(t)
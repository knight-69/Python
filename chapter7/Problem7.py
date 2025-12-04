n = int(input("Enter the number : "))
for i in range(1, n+1):
    print(" "*(n-i),end="")    # by adding end="" it does not add a new line
    print("*"*(2*i-1),end="") 
    print("")
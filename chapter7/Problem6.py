# 5! = 1 x 2 x 3 x 4 x 5    # it is called a factorial form

n = int(input("Enter the number : "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"the factorical of {n} is {product}")
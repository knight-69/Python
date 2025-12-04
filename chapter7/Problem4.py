a = int(input("Enter your number"))

for i in range(2,a) :
    if(a%i) == 0 :
         print("it is a not prime number")
    break
else:
    print("it is not a prime number")
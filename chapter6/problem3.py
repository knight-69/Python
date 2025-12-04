# my code (this give every comment is spam)
comment = input("Enter your comment :")

if("Make a lot of money","buy now", "subscribe this", "click this"):
    print("this is a spam")

else:
    print("this is not a spam")



#harry method
p1 = "Make a lot of money"
p2 = "buy now"
p3 =  "subscribe this"
p4 = "click this"

message = input("Enter your comment : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")
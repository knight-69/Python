# # This was my answer 
# Name = input("Enter Your name :" )
# Date = input("Enter Date :")
 
# print(f"Dear {Name} You are selected! {Date}")


# this was harry answer
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> ''' 

print(letter.replace("<|Name|>","Harry").replace("<|Date|>","20 Nov 2025"))



#the answer given by gemini
# # 1. Define the template (Harry's part)
# letter = ''' 
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 

# # 2. Get the data (Your part)
# user_name = input("Enter Your Name: ")
# user_date = input("Enter Date: ")

# # 3. Replace and Print (The logic part)
# # Notice we put user_name variable inside the replace function
# new_letter = letter.replace("<|Name|>", user_name).replace("<|Date|>", user_date)

# print(new_letter)
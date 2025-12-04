# d = {} # Empty dictionary
marks = {
    "harry":100,
    "Subham":56,
    "rohan":23,
    0 : "harry"
    
}

# print(marks.items())  # put item in barkets
# print(marks.keys()) # it prints the left side which is called keys .
# print(marks.values()) #  it print the right side which is called the values.
# marks.update({"harry":99 , "Renkuka":100}) # it updates the value of the the existing dictonary and also can add value later after creating dictonary.
# print(marks)

# it return the the value if it exist in dictonary if the search word is not it give none as the output.
print(marks.get("amit")) 
print(marks.get("harry"))
#important
# the difference b/w both two are is that if the input is same as in the dictionary is same th result will be the same
# but if the input is not from the dictonary this will be the difference 
print(marks.get("harry2")) # prints None
print(marks["harry2"]) # Returns an error
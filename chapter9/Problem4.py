word = "Donkey"


with open("file4.txt","r") as f:
    content = f.read()


contentNew = content.replace(word,"######")

with open("file4.txt" ,"w") as f:
    content = f.write(contentNew)
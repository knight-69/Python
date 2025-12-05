with open("old.txt" ,"r") as f:
    content = f.read()

with open ('renamed_by_pyhton.txt',"w") as f:
    f.write(content)

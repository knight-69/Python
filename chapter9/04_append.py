'''
Type of function

r - open for reading 
w - open for writing  
a - open for appending #it is mode in which we can add end of file.
+  - open for updating. 
'rb' will open for read in binary mode. 
'rt' will open for read in text mode. 


'''
st =" hey this is from 02_file_write.py"

f = open("myfile.txt","a")

f.write(st)

f.close()
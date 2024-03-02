f = open("demo.txt","w")#if the file provided in the open mode does not exists then write mode asnd append mode will create a new file.
#f = open("demo.txt", "a")

'''read'''
#data = f.read() #to read full file
# data = f.read(5) # This is used to read the first 5 letters
#line1 = f.readline() #this is read first line
#peinr(line1)
#line2 = f.readline() #this is read first line
#print(line2)

'''write'''
f.write("I want to learn Js") #if we do this with write mode then the file content will be deleted and the new data will be added to the file
#f.write("Then i will fo to react") # if we do this with append(a) mode then new data will be appended to the end of the file


'''print(data) # this is for read 
print(type(data))'''

f.close() #closing the file 

'''This is link for combining different modes'''
# https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function

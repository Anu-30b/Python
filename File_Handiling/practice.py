'''
Create a new file "practice.txt" using python. Add the following content
Hi everyone
we are learning File I/O
using Java.
I kine programming in Java.


WAF that replace all occurances of "java" with "python" in the above file.

Search that replace all occurences of "java" with "python"
'''
# To create the file
#with open("practice.txt","w") as f:
#    f.write("Hi everyone\nwe are learning File I/O\n")
#    f.write("using Java\nI line programming in Java")

# Chaging the data
'''with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("pratice.txt","w") as f:
    f.write(new_data)'''

# To find the word learning
'''word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if data.find(word) != -1:
        print("found")
    else:
        print("not found")'''

#To find the first occurence of the word learning and its line number
'''def check_for_line():
    word = "learning"
    data = True 
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
            line_no += 1
    return -1

print(check_for_line())'''


# From the file contaning numbers seperated by comma, print the count of even number
with open("Numbers.txt","r") as f:
    data = f.read()
    print(data)

    count = 0
    nums = data.split(",")
    for val in nums:
        if int(val) % 2 == 0:
            count+= 1
    print(count)


    '''num = ""
    for i in range(len(data)):
        if data[i] == ",":
            print(int(num))
            num = ""
        else:
            num += data[i]'''
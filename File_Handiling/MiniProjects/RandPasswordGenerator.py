import random
import string

password_len = 12
#print(string.ascii_letters)
charValues= string.ascii_letters + string.digits + string.punctuation
#print(charValues)

#list comprehension [function for i in range(n)]

password = [random.choice(charValues) for i in range(password_len)]


'''using loop'''
# password = ""
# for i in range(password_len):
#     password += random.choice(charValues)

print("Your random password string is ", "".join(password))
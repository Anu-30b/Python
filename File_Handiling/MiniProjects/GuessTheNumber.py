import random

target = random.randint(1,100)

i = 0
print("You will have 6 chances to guess the number")
while i<=6:
    n = input("Guess the target number between(1 to 100) or Quit(Q): ")
    if n == "Q":
        break 
    n = int(n)
    if n == target:
        print("Success: Corect Guess!!!")
        break 
    elif(n < target):
        print("Your number was too small.. Take a bigger guess")
    else:
        print("Your number was too Big.. Take a smaller guess")
    i += 1
    
print("----GAME OVER----")
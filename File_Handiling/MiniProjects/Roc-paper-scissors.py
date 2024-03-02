import random

Values = ["R", "P", "S"]

machine_score = 0
user_score = 0
n = 3
print("--------------Only three chances-----------------------------")
while n>0 :
    Machine = random.choice(Values)
    userInput = input("Enter Rock(R) or paper(P) or scissors(S) ")
    if (userInput == "R" and Machine == "P") or (userInput == "P" and Machine == "S") or (userInput == "S" and Machine == "R"):
        machine_score += 1 
        print("Machine: ", Machine, " and User: ", userInput, "So machine will get a point")
        n -= 1
    elif (userInput == "R" and Machine == "S") or (userInput == "P" and Machine == "R") or (userInput == "S" and Machine == "P"):
        user_score += 1
        print("Machine: ", Machine, " and User: ", userInput, "So user will get a point")
        n -= 1
    elif userInput == Machine:
        print("No one will get the point because both choosen the same input")
        n -= 1
    else:
        print("Please Enter P or R or S only")
print(machine_score, user_score)
if machine_score == user_score:
    print("------------DRAW----------------")
if machine_score > user_score:
    print("----MACHINE WON THE GAME----")
elif machine_score < user_score:
    print("----YOU WON THE GAME----") 

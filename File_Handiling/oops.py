
#Abstratction
'''class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = Car()
car1.start() #This will print only the neccessary details that is whether car will start or not and hides the details that if clucth and acceleratir is being used or not.'''

#Practice Ques
#Create Account class with 2 attributes - balance and account no.
#Create methods for debit, credit and printing the balance.

'''class Bank:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance = self.balance - amount
        print("Total balance in the account number ",self.acc_no, " is ", self.balance)

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Total balance in the account number ",self.acc_no, " is ", self.balance)

    def total_balance(self):
        print("Total balance is ", self.balance)

acc = Bank(50000, 1234567)
acc.debit(1000)
acc.credit(2000)
acc.total_balance()'''


# Inheritance 

'''Single Inheritance'''
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started")
    
#     @staticmethod 
#     def stop():
#         print("Car Stopped..")

# class ToyotaCar(Car): #ToyotaCar inherits the properties of Car
#     def __init__(self, brand):
#         self.brand= brand
    
# car1 = ToyotaCar("fortuner") 
# car2 = ToyotaCar("prius") 

# print(car1.color)

'''Multi-level Inheritance'''

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started")
    
#     @staticmethod 
#     def stop():
#         print("Car Stopped..")

# class ToyotaCar(Car): #ToyotaCar inherits the properties of Car
#     def __init__(self, brand):
#         self.brand= brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("disel")
# car1.start()

'''Multiple Inherutance'''
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

'''Super method -- It is used to access methods  of parent class
The most common use of the super keyword is to eliminate the confusion between superclasses and subclasses that have methods with the same name. '''

# class Car:
#     def __init__(self, type):
#         self.type = type 
    
#     @staticmethod 
#     def start():
#         print("car Started..")
    
#     @staticmethod 
#     def stop():
#         print("car Stopped...")

# class ToyotaCar(Car):
    
#     def __init__(self, type, name):
#         super().__init__(type) #This will call the contructor of the parent class
#         self.name = name 

# car1 = ToyotaCar("prius","electric") # This will call the constructor of the child class.
# print(car1.type) #If we do this without super calss we wil get an error becuse the child can call the constructor method in the parent class so to call it we use super method




# class Person:
#     name = "anonymous"

#     # def changeName(self, name):
#     #     #self.name = name  #This is used to just change the name using object
#     #     self.__class__.name = name #This is used to change the name using class

#     @classmethod 
#     def changeName(clas, name):
#         clas.name = name
        
# p1 = Person()
# p1.changeName("rahul Kumar")
# print(p1.name)
# print(Person.name)


class Student:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che 
        self.math = math 
        self.percentage = str((self.phy+self.che+self.math)/3)

stu1 = Student(98,97,99)


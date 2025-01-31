# Practice Python – Problem 1
# • Problem 1: Develop an application that asks the user
# for her/his name, and then greets them with their
# name.

class User:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome! to NCI!!")

user_name = input("What is your name? ")

s1 = User(user_name)
s1.greet()

       
        

''' Random method'''
from array import array
import numbers
import random

"""
print("Guess the computer's choice to win a price")
a = [1,2,3,4,5,6,7,8]
print("select a number from", a)
random.shuffle(a)
com_choice = random.choice(a)
user_input = int(input("Enter your a number of your choice: \n:>"))
if user_input == com_choice:
    print("YO HAVE WON THE LOTERY PRIZE!CONGRATULATION!!!")
else: 
    if user_input > com_choice:
        print("Too high")
    else: 
        print("Too low")
    print("You 'lose' try again to win...")

"""


# print("\nGuess the computer's choice to win the ROCK-PAPER-SCISSORS GAME! \n")
# x = ["rock", "paper" , "scissors"]
# print("Enter a word from" , x)
# random.shuffle(x)
# com_choice = random.choice(x)
# user_input = input("Enter your a word of your choice form the list above: \n:>").lower()
# if user_input in x:
#     if user_input == com_choice:
#         print("You have a draw with the computer")
#         print("your choice:", user_input, "computer's choice:", com_choice)
#     elif user_input == x[0] and com_choice == x[2]:
#         print("YES! YOU WIN")
#         print("your choice:", user_input, "computer's choice:", com_choice)
#     elif user_input == x[2] and com_choice == x[1]:
#         print("YES! YOU WIN")
#         print("your choice:", user_input, "computer's choice:", com_choice)
#     elif user_input == x[1] and com_choice == x[0]:
#         print("YES! YOU WIN")
#         print("your choice:", user_input, "computer's choice:", com_choice)
#     else:
        
#         print('HAHA! COMPUTER WINS!.....\n')
#         print("your choice:", user_input, "computer's choice:", com_choice)
#         print('\nKeep on trying')
# else: 
#     print("DON YOU KNOW HOW TO READ? type a correct word and play again!")

# b = random.shuffle(a)
# print(b)
# c = random.sample(a,3)
# print(c)


# def factorial(n):
#     if n==1:
#         return 1
#     if n==0:
#         return 1
#     recurse = n * factorial(n-1)
#     print(recurse)
#     return recurse
# factorial(5)


# print('x')

# if 4>5:
#     print(7)

# print(4)


# score = int(input("Enter your examination score:\n:>"))
# print(type(score))
# if score <= 100:
#     if score >= 90:
#         print('Your result grade is: "A"')
#     elif score >= 80:
#         print('Your result grade is: "B"')
#     elif score >= 70:
#         print('Your result grade is: "C"')
#     elif score >= 60:
#         print('Your result grade is: "D"')
#     elif score >= 50:
#         print('Your result grade is: "E"')
#     elif score >= 40:
#         print('Your result grade is: "F"')
#     else:
#         print("comrade na skill sure you pass")
# else:
#     print("Oya come and go to harvard university")


'''Lambda functions are annoynmous single expression that can have any amount of parameters/arguments'''

# my_string = "this day is lovely"
# print(my_string)
# a = list(map(lambda f: f.upper(), my_string))
# print("".join(a))

''' 
looping is away of going over ablock of code as long as the conditions are met...
FOR LOOP : goes over a block of code for either a period of time or for a range

range is a function that give you numbers within a starting point and and end point
range(start,stop,steps)

'''


# for i in range(10):
#     if i == 5:
#         # break
#         continue
#     print(i)

count_1 = 0
for i in range(90,121):
    if i%2 == 1:
        count_1+=1
        print(i)
print("\nTotal odd numbers is:", count_1)


count_2 = 0
set_numbers = [1,2,3,4,15,22,21,33,50,55,72,66,95]

for i in set_numbers:
    if i%3 ==0 or i%5==0:
        count_2+=1
        print(i)
print("\nTotal numbers for multiple of '5' and '3' is:", count_2)


user_interger = int(input("enter any whoe number of your choice\n:>"))


'''h=1
while h<=10:
    print (h)
    h +=1

h=1
while h<=10:
    h+=1
    print (h)
'''

import random
''' 
print("Guess the computer's choice to win a price")
a = [1,2,3,4,5,6,7,8]
print("select a number from", a)
random.shuffle(a)
trial =3
score =0

while trial>0:
    print("\nselect a number from:", a)
    com_choice = random.choice(a)
    user = int(input("Enter your a number of your choice: \n:>"))
    if user == com_choice:
        print("YOU WIN!")
        score+=2
        trial +1
        print(f"you have won an extra trial")
        print(f"{trial} trial(s) left")
    else:
        if user > com_choice:
            print("too high")
        else:
            print("Too low")
        trial-=1
        print(f"{trial} trial(s) left")
print(f"\n You scored {score} points")
print("\n GAME OVER!")
'''

options =['r','p','s']
trial =3
score =0
while trial >0:
    print("\n Select R for rock, P for paper and S for Scissors.")
    com_choice = random.choice(options)
    player_choice = input(">").lower()
    if player_choice in options:
        if player_choice == options[0] and com_choice == options[2]:
            print("You win")
            print("computer choose", com_choice)
            trial+= 1
            score +=2
        elif player_choice== options[2] and com_choice == options[1]:
            print("You win")
            print("computer choose", com_choice)
            trial+= 1
            score +=2
        elif player_choice== options[1] and com_choice == options[0]:
            print("You win")
            print("computer choose", com_choice)
            trial+= 1
            score +=2
        elif player_choice== com_choice:
            print("it's a tie")
        else:
            print("you losose")
            print('computer choose', com_choice.title())
            trial-=1
    else:
        print("invalid input")
        trial-=1
    print(f'{trial} trials left')
print("Game over")
print("you scored", score)





# com_choice = random.choice(a)

# user_input = int(input("Enter your a number of your choice: \n:>"))
# if user_input == com_choice:
#     print("YO HAVE WON THE LOTERY PRIZE!CONGRATULATION!!!")
# else: 
#     if user_input > com_choice:
#         print("Too high")
#     else: 
#         print("Too low")
#     print("You 'lose' try again to win...")

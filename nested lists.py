import random

rock = '''

     -------
----|       |
           |
           |
-----------/
'''

paper = '''

     -------
----|  ______|
______________|
_____________|
-----------/

'''
game_images = [rock, papers, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lost!")
elif computer_choice > user_choice:
    print("Computer wins!")
elif computer_choice == user_choice:
    print("It is a draw")
else:
    print("You typed an invalid number, and you lost!")
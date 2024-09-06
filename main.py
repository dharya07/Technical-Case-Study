import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
    print("Computer chose:")
    print(game_images[computer_choice])
    if user_choice == computer_choice:
        print("Draw")
    elif user_choice == 0:
        if computer_choice == 1:
            print("You lose")
        else:
            print("You win!")
    elif user_choice == 1:
        if computer_choice == 2:
            print("You lose")
        else:
            print("You win!")
    elif user_choice == 2:
        if computer_choice == 0:
            print("You lose")
        else:
            print("You win!")
else:
    print("You enetered an invalid choice! You lose!")

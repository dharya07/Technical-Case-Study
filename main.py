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

def get_user_choice():
    while True:
        try:
            choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

user_choice = get_user_choice()
computer_choice = random.randint(0, 2)

print("You chose:")
print(game_images[user_choice])
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")

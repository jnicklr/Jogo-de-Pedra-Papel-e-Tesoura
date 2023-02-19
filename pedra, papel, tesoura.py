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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

if (user_choice == 2) or (user_choice == 1) or (user_choice == 0):

    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    else:
        print(scissors)

    computer_choice = random.randint(0, 2)

    print("Computer choose: ")

    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)

    if (computer_choice == user_choice):
        print("It\'s a tie.")
    elif (computer_choice == 0) and (user_choice == 2):
        print("You lose.")
    elif (computer_choice == 1) and (user_choice == 0):
        print("You lose.")
    elif (computer_choice == 2) and (user_choice == 1):
        print("You lose.")
    else:
        print("You won.")
else:
    print("Invalid choice!")

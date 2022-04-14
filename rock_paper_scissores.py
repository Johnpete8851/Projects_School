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

#Write your code below this line 👇
game_image=[rock,paper,scissors]

user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_image[user_choice])

computer_choice=random.randint(0,2)
print("computer choose")
print(game_image[computer_choice])

if user_choice==0 and computer_choice==2:
  print("compute wins")
elif user_choice==0 and computer_choice==2:
  print("you wins")
elif user_choice==1 and computer_choice==1:
  print("draw")
elif user_choice==0 and computer_choice==0:
  print("draw")
elif user_choice==0 and computer_choice==2:
  print("you wins")
elif user_choice==1 and computer_choice==2:
  print("computer win")
elif user_choice==2 and computer_choice==1:
  print("you win")
elif user_choice==2 and computer_choice==2:
  print("draw")
elif user_choice==1 and computer_choice==0:
  print("draw")
elif user_choice==2 and computer_choice==0:
  print("computer wins")
















# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#Write your code below this line 👇
bill=0

#small
if size=="S":
    bill=15
if add_pepperoni=="Y":
    bill+=2
if extra_cheese=="Y":
    bill+=1

#medium
if size=="M":
    bill=20
if add_pepperoni=="Y":
    bill+=3
if extra_cheese=="Y":
    bill+=1

#large
if size=="L":
    bill=25
if add_pepperoni=="Y":
    bill+=3
if extra_cheese=="Y":
    bill+=1
print(f"Your final bill is: ${bill}")

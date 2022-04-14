# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lenght_list=len(names)
import random
names_togo=random.randint(0,lenght_list-1)
names_will_be=names[names_togo]
print(names_will_be,"is going to buy the meal today!")

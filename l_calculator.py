# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name_comb= name1 + name2
#Write your code below this line 👇
t=r=u=e=0
name_comb.count("t")
name_comb.count("r")
name_comb.count("u")
name_comb.count("e")
name_comb.count("t")+name_comb.count("r")+name_comb.count("u")+name_comb.count("e")
ture_total=name_comb.count("t")+name_comb.count("r")+name_comb.count("u")+name_comb.count("e")

name_comb.count("l")
name_comb.count("o")
name_comb.count("v")
name_comb.count("e")
name_comb.count("l")+name_comb.count("o")+name_comb.count("v")+name_comb.count("e")
love_total=name_comb.count("l")+name_comb.count("o")+name_comb.count("v")+name_comb.count("e")
love_score= int(str(ture_total) + str(love_total))
if int(love_score<10) or int(love_score>90):
    print("Your score is",love_score, "you go together like coke and mentos.")
elif int(love_score>=40) and int(love_score<=50):
    print("Your score is", love_score, "you are alright together.")
else:
    print("Your love score",love_score)

import sys
import random
 
    
print("")
playerchoice=input('ENTER....\n1 for rock,\n2 for paper,\n3 for scissors:\n\n')


player=int(playerchoice)

if player<1 | player>3:
    sys.exit("you must enter 1,2,3")

computerchoice=random.choice("123")
computer= int(computerchoice)

print("")
print("you choose"+playerchoice+".")
print("python choose"+computerchoice+".")
print("")

if player==1| computer==3:
    print("you win")
elif player==2 | computer==1:
    print("you win")
elif player==3 and computer==2:
    print("you win")
elif computer==player:
    print("tie")
else:
    print("python win")




 
 
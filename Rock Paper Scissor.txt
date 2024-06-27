import random

def choose(choice):
    if choice==1:
        return "SNAKE"
    elif choice==2:
        return "WATER"
    elif choice==3: 
        return "GUN"
    
player=int(input("Enter 1 for SNAKE\nEnter 2 for WATER\nEnter 3 for GUN\n"))
computer=random.randint(1,3)

print("you choose",choose(player))
print("computer choose",choose(computer))

if (player==computer):
    print("IT'S A DRAW")
elif((player==1 and computer==2)or (player==2 and computer==3)or player==3 and computer==1):
    print("YOU WON")
else:
    print("YOU lOSE")   
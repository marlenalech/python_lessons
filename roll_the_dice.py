import random
def diceroll():
    randomNum = random.randint(1,6)
    secondrandomNum = random.randint(1,6)
    return randomNum, secondrandomNum

while True:  
    x = input("Roll the dice? (y/n)")
    if x.lower() == "y": 
        print(diceroll())
    elif x.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
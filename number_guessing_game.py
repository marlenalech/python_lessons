import random

ran = random.randint(1, 100)

while True:
    try:    
        guess = int(input("Guess the number from 1 to 100:"))

        if ran < guess:
            print("Too much")
        elif ran > guess:
            print("Too low")
        else:
            print(f"Well done, number is: {ran}")
            break
    except ValueError:
        print("Please enter a valid number")

print(ran)
import random

choices = ("r","p","s")
emojis = {"r":"🪨", "p":"📃", "s":"✂️"}

while True:
    choice = input("Rock, paper or scissors? (r/p/s)").lower()
    if choice not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print(f"You chose {emojis[choice]}")
    print(f"Computer chose {emojis[computer]}")

    if choice == computer:
        print("Tie!")
    elif (
        (choice == "r" and computer == "s") or 
        (choice == "s" and computer == "p") or 
        (choice == "p" and computer == "r")):
        print("You win!")
    else:
        print("You lose!")

    should_continue = input("Continue? (y/n)").lower()
    if should_continue == "n":
      break
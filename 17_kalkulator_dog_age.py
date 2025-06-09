#convert dog age to human age

dog_age = float(input("Podaj wiek psa: "))

if dog_age < 0:
    print("Nieprawidłowe dane!")
elif dog_age <= 1:
    human_age = dog_age*15
    print(f"ludzkie: {human_age}, psie: {dog_age}")
elif dog_age <= 2:
    human_age = 15 + (dog_age - 1) * 9
    print(f"ludzkie: {human_age}, psie: {dog_age}")
else:
    human_age = 24 + (dog_age - 2) * 5
    print(f"ludzkie: {human_age}, psie: {dog_age}")
#n! = 1*2*3*...*(n-1)*n
i = 1
silnia = input("Wprowadź silnię: ")
wynik = 1

while i <= int(silnia):
    wynik *= i
    i += 1
else:
    print("Koniec pętli")

print(f"{silnia}! = {wynik}")
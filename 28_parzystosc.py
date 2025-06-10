n = int(input("Określ zakres liczbowy: "))
parzyste = []
nieparzyste = []
for x in range(1, n+1):
    if x % 2 == 0:
        parzyste.append(x)
    else:
        nieparzyste.append(x)

print(f"Parzyste liczby: {parzyste}")
print(f"Nieparzyste liczby: {nieparzyste}")
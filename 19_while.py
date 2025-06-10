num = 0
maxnum = int(input("Wprowadź maksymalną wartość: "))
suma = 0

while num <= maxnum:
    suma += num
    num += 1
else:
    print("Koniec pętli while")

print(f"Suma liczb od 0 do {maxnum} to {suma}")
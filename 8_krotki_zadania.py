krotka = (50, 100, 150, 200, 250)
print(type(krotka))
print(len(krotka))
print(krotka[len(krotka)-1])
print(krotka[2:4])
print(krotka[-3])

wydatki = (100, 200, 300, 400, 500, 600)
suma = 0

for x in wydatki:
    suma += x

print("suma wydatków: ", suma)
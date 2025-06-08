lista_zakupow = ["apple","kiwi","strawberry","banana","pineapple","blueberry"]

print(type(lista_zakupow))
print(lista_zakupow)

print(list[0])
print(len(lista_zakupow))
print(lista_zakupow[4])
print(lista_zakupow[len(lista_zakupow)-1])

print(lista_zakupow[-1])
print(lista_zakupow[-2])

print(lista_zakupow[1:4])
print(lista_zakupow[2:])
print(lista_zakupow[::2])

del lista_zakupow[1]
print(lista_zakupow)

print(99 in lista_zakupow)
print("apple" in lista_zakupow)
lista_zakupow.append(1)
print(1 in lista_zakupow)
print(lista_zakupow)

del lista_zakupow[-1]
print(lista_zakupow)

if "banana" in lista_zakupow:
    print("kupić: " + lista_zakupow[2])

for x in lista_zakupow:
    print(x)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(len(matrix))
print(len(matrix[0]))

print(matrix[1][2])

row4 = [10,11,12]

matrix.extend(row4)
print(matrix)

del matrix[3:]
print(matrix)

matrix += row4
print(matrix)
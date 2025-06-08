data = [0,1,2,3,4,5,6]
print(len(data))
del data[1]
print(len(data))

if 3 in data:
    print("3 jest na liście")

for x in data:
    print("wartości w liście: ")
    print(x)

for x in data:
    print("wartości w liście, pomnożone przez 2: ")
    print(x*2)
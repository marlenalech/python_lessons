squares = []

n = int(input("Wprowadź maksymalną ilość kwadratów: "))

for x in range(1, n+1):
    sqr = x**2
    squares.append(sqr)
if squares:
    print(squares)
else:
    print("Lista jest pusta")
    
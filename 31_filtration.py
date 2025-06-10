num = [1,2,3,4,5,6,7,8,9,10]

for x in num:
    if x % 2 == 0:
        continue
    if x > 8:
        break
    if x % 2 != 0 or x < 8:
        print("Kwadraty: ", x**2)
else:
    print("Koniec działania programu")
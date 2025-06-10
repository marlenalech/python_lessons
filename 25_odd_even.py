num = [-4,-3,-2,-1,0,1,2,3,4]

for x in num:
    if x == 0:
        print("Zero jest parzyste")
    elif x % 2 == 0:
        print(f"{x} jest parzyste")
    else:
        print("Nieparzysta liczba")
    
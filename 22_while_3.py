num_of_el = int(input("Wprowadź liczbę elementów: "))

sum = 0

if num_of_el>0:
    i = num_of_el

    while i>0:
        i -= 1

        num = float(input("Podaj liczbę: "))
        sum += num
    avg = sum / num_of_el
    print(f"Średnia to: {avg}")
else:
    print("Nie można obliczyć średniej")
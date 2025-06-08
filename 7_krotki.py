kwiaty = ("tulipan", "mak", "chaber", "róża")
print(kwiaty)
print(type(kwiaty))
print(len(kwiaty))

kwiat = "mak",
print(kwiat)
print(type(kwiat))
print(len(kwiat))

empty = ()
print(empty)
print(type(empty))
print(len(empty))

print(kwiaty[1])
print(kwiaty[-1])
print(kwiaty[2:])
print(kwiaty[:2])
print(kwiaty[::2])
print(kwiaty[1:4])

del empty

if "mak" in kwiaty:
    print("mamy maj! <3")
mojset = {1,10,100,1000}

mojset.add(10000)

mojset.discard(1)

print(type(mojset))
print(mojset)

for x in mojset:
    print(x)

frozen = frozenset(mojset)

print(type(frozen))

# frozen.add(1) błąd

for x in frozen:
    print(x)
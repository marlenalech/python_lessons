numbers = [-3,-2,-1,0,1,2,3]
set = {-1}

for x in numbers:
    if x % 2 != 0:
        set.add(x)

for y in set:
    print(y)
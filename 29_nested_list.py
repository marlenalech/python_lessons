nested_list = [
    [1,2,3],
    ["a","b","c"],
    [True, False, True],
]

for list in nested_list:
    for x in list:
        print(x)
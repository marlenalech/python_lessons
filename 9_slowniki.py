kontakty = {
    "Anna" : "anna@example.com",
    "Mateusz" : "mateusz@example.com",
    "Rafał" : "rafal@example.com",
    "Katarzyna" : "katarzyna@example.com"
}

kontakty["Damian"] = "damian@example.com"

print(kontakty)
print(kontakty["Anna"])
print(type(kontakty))
print(len(kontakty))

print(kontakty.keys())
print(kontakty.values())

for x in kontakty:
    print(x + "" + kontakty[x])

for x, y in kontakty.items():
    print(x, y)
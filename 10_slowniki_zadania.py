config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : "12345"
}

print(len(config))
print(config["dbType"])
for x, y in config.items():
    print("Klucz w config: "+ x + " z wartością " + y)
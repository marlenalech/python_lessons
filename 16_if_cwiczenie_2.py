#check if candidate is potential programmer

exp = 1
languages = ["python","typescript","javascript","html","css"]
contractType = "b2b"

if exp >= 2 and "python" in languages:
    print("its good")
    if contractType == "b2b" or "employment":
        print("You've got this job 💪")
    else:
        print("Sorry, try next time <3")
else:
    print("Sorry, try next time <3")
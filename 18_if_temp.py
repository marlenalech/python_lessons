raining = True
haveUmbrella = True 
temperature = 9

if temperature >= 40 or temperature <= 0:
    print(f"Zostań w domu, warunki niesprzyjające. Temperatura: {temperature}")
elif temperature > 0 and temperature < 10 and raining and haveUmbrella:
    print("Możesz wyjść z parasolką")
elif temperature > 10 and raining == False:
    print("Możesz wyjść bez parasolki")
else:
    print("Zostań w domu")
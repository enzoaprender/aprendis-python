while True:
    temperatura = float(input("Digite a temperatura em Celsius: "))
    if temperatura<10:
        print("A temperatura está muito baixa.")
    elif temperatura<23:
        print("A temperatura está agradável.")
    else:
        print("A temperatura está muito alta.")
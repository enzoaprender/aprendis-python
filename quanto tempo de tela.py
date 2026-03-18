while True:
    horas_de_estudo = int(input("Quantas horas de estudo por dia? "))
    horas_de_lazer = int(input("Quantas horas de lazer por dia? "))
    horas_de_Sono = int(input("Quantas horas de sono por dia? "))

    if horas_de_estudo<3:
        print("tente estudar mais")
    elif horas_de_lazer>=5:
        print("tente diminuir o tempo de lazer")
    elif horas_de_Sono>7:
        print("tente dormir mais")

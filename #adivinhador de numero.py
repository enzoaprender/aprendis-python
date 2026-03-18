#adivinhador de numero
import random
print("Bem-vindo ao jogo de adivinhação!")
numero_secreto = random.randint(1, 100)
tentativas = 0
while True:
    palpite = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
     print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")


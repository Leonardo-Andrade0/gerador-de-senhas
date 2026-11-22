import random
import string

caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits

while True:
    try:
        tamanho = int(input("Tamanho da senha (mínimo 4): "))
        if tamanho >= 4:
            break
        print("O tamanho mínimo é 4.")
    except ValueError:
        print("Digite um número inteiro válido.")

senha = ""
for i in range(tamanho):
    senha = senha + random.choice(caracteres)

print("Sua senha:", senha)
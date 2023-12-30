import random

letras = input("Seja bem vindo ao gerador de senhas \nQuantas letras a sua senha deve ter?\n")
simbolos = input("Quantos simbolos a sua senha deve ter?\n")
numeros = input("Quantos numeros a sua senha deve ter?\n")
senha = []

for char in range(1, int(letras) + 1):
    senha.append(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))

for char in range(1, int(simbolos) + 1):
    senha.append(random.choice("!@#$%&*()"))

for char in range(1, int(numeros) + 1): 
    senha.append(random.choice("0123456789"))

random.shuffle(senha)
senha_final = "".join(senha)
print(f"Sua senha é: {senha_final}")
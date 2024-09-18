# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.
número = int(input("Fatorial de: "))
resultado = 1
for i in range(1,número + 1):
    resultado *=i
print("O fatorial de", número, "é", resultado)

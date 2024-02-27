texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

# range com for

for numero in range(0,51,5):
    print(numero)
print()

# while

tipo_conta = -1

while tipo_conta != 0:
    tipo_conta = int(input("Selecione o tipo de conta:\n[1] - Sacar \n[2] - Extrato\n[0] - Sair "))

    if tipo_conta == 1:
        print("Sacar")
    elif tipo_conta ==2:
        print("Extrato")

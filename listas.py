frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("Python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]

print(numeros)
print(letras)
print(carro)

print(letras[0])
print(letras[0:2])
print(carro[1])

print(numeros[-1])

#listas aninhadas 

matriz = [
    [1, "a", 3],
    ["b", 4, 5],
    [6, 5, "c"]
]

print(matriz[0][0])

for _ in carro:
    print(carro)


list = [1, 2, 3, 4, 5, 6, 100, 200, 7]

pares = []

for numero in list:
    if numero %2 == 0:
        pares.append(numero)
print(pares)

print(set([1 , 2, 3, 3, 5, 6 ,7]))

print(set("Abacaxi"))

linguagens = {"Python", "Python", "Java", "C"}

print(linguagens)

# para acessar valores é necessário converter em lista
lista = list(linguagens)
print(lista)


for ling in linguagens:
    print(ling)

conjunto_a = {1, 2, 3}
conjunto_B = {3, 4, 2}
conjunto_c = {9, 10}

# union
#novo_conjunto = conjunto_a.union(conjunto_B)

# print(novo_conjunto)

# intersection
# novo_conjunto2 = conjunto_a.intersection(conjunto_B)

# print(novo_conjunto2)

# difference
novo_conjunto3 = conjunto_a.difference(conjunto_B) # trás do conjunto a o que não tem no conjunto B

print(novo_conjunto3)

# symmetric_difference
# trás tudo que não é comum entre os dois conjuntos
conjunto_a.symmetric_difference(conjunto_B)

# issuperset
print(conjunto_a.issuperset(conjunto_B)) #False
print(conjunto_B.issuperset(conjunto_a)) #False

print(conjunto_a.isdisjoint(conjunto_c)) #True

#add
sorteio = {10, 20, 30}
sorteio.add(32)

print(sorteio)

# in

10 in sorteio # true
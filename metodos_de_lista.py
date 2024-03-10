# append
list = []

obj1 = list.append("Python")
obj2 = list.append(True)
obj3 = list.append(750)
obj4 = list.append([1, 2, 3,4 ])
print(list)

lista2 = [1, "Python",[1, 50, 100]]

# copy
lista2.copy()

print(lista2)

print(id(list), id(lista2))

# count
print(list.count(750))

# extend (nao elimina valores duplicados)
linguagens = ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)

# index retorna a posicao da ocorrencias
print(linguagens.index("java"))

# pop

linguagens.pop(0)

print(linguagens)

linguagens.reverse()

print(linguagens)

# sort ordena #reverse = True trás de trás pra frente
linguagens.sort()

# ordenando por tamanho

linguagens.sort(key = lambda x: len(x))

# len
len(linguagens) # 5

# sorted
sorted(linguagens, key = lambda x: len(x))
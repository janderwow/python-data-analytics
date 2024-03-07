#append
list = []

obj1 = list.append("Python")
obj2 = list.append(True)
obj3 = list.append(750)
obj4 = list.append([1, 2, 3,4 ])
print(list)

lista2 = [1, "Python",[1, 50, 100]]

lista2.copy()

print(lista2)

print(id(list), id(lista2))

print(list.count(750))
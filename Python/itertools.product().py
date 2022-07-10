"""
itertools.product()

https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=false


"""


from itertools import product

a = [1, 2, 3]
b = [3, 4, 5, 6, 7]

print(list(product([1, 2, 3, 4],repeat = 2)))

"""

loop = len(a) * len(b)

x = 0
z = 0
lista1 = []

for i in range(loop):
    lista = []

    lista.append(a[x])
    lista.append(b[z])
    z += 1
    tupla = tuple(lista)
    lista1.append(tupla)
    lista.clear()
    if z == len(b):
        z = 0
        x += 1


print(lista1)

"""
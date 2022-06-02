# so consegui fazer passar consultando pois preciso estudar testes

l = set(arr)
l1 = []

for i in l:
    l1.append(i)
l1.sort(reverse=True)
print(l1[1])


"""
n = 5
A = [2, 3, 6, 6, 5]


A = sorted(set(A))
A.remove(max(A))

print(max(A))
"""


"""
n = 10
A = []

for i in range(n):
    A.append(i)
A = sorted(set(A))
A.remove(max(A))
print(max(A))
"""
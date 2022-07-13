n = input()

n = set(input().split())

b = input()

b = set(input().split())

c = n.union(b)
print(len(c))

"""
n = 9
n = "1 2 3 4 5 6 7 8 9"
b = 9
b = "10 1 2 3 11 21 55 6 8"


c = list(n + b)
print(c)
c = set(c)
print(len(c))
"""
"""
s = set("1 2 3 4 5 6 7 8 9")
print (s.union("10 1 2 3 11 21 55 6 8"))
set([1 2 3 4 5 6 7 8 9])

"""
"""
n = set(1,2, 3, 4, 4, 4)
b = n.union()
print(len(b))
"""


"""

print( s.union(set(['R', 'a', 'n', 'k'])))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print (s.union(['R', 'a', 'n', 'k']))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print (s.union(enumerate(['R', 'a', 'n', 'k'])))
set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

print (s.union({"Rank":1}))
set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

s | set("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])
"""

"""
n = input()

n = input().split()

b = input()

b = input().split()


c = n + b
c = list(set(c))
print(len(c))


n = input()

n = set(input().split())

b = input()

b = set(input().split())


c = n.union(b)
c = list(set(c))
print(len(c))

"""


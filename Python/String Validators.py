s = 'qA2'

n1 = 0
n10 = 0
for l in s:
    n10 += 1
    if n1 == 0:
        if (l.isalnum()) == True:
            print(True)
            n1 +=1
        if len(s) == n10 and n1 == 0:
            print(False)

n2 = 0
n20 = 0
for l in s:
    n20 += 1
    if n2 == 0:
        if (l.isalpha()) == True:
            print(True)
            n2 +=1
        if len(s) == n20 and n2 == 0:
            print(False)

n3 = 0
n30 = 0
for l in s:
    n30 += 1
    if n3 == 0:
        if (l.isdigit()) == True:
            print(True)
            n3 +=1
        if len(s) == n30 and n3 == 0:
            print(False)

n4 = 0
n40 = 0
for l in s:
    n40 += 1
    if n4 == 0:
        if (l.islower()) == True:
            print(True)
            n4 +=1
        if len(s) == n40 and n4 == 0:
            print(False)

n5 = 0
n50= 0
for l in s:
    n50 += 1
    if n5 == 0:
        if (l.isupper()) == True:
            print(True)
            n5 +=1
        if len(s) == n50 and n5 == 0:
            print(False)


s = '4pablo henrique 7santos da silva 54455'

def solve(s):

    lista = []

    for i, l in enumerate(s):

        if i == 0:
            lista.append(s[i].capitalize())
        else:
            if s[i].isalpha() == True and s[i-1] in ' ':
                lista.append(s[i].capitalize())
            else:
                lista.append(s[i])
    s = ''.join(lista)
    print(s)
    return s

print(solve(s))
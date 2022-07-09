string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 4

def wrap(string, max_width):
    lista = []
    n = 0
    for i in range(0, len(string)):
        n += 1
        lista.append(string[i])
        if n == max_width:
            lista.append('\n')
            n = 0

    string = ''.join(lista)

    return string


print(wrap(string, max_width))
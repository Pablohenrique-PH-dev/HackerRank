first = 'Pablo'
last = 'Silva'

def print_full_name(first, last):
    saida = ('Hello {} {}! You just delved into python.'.format(first, last))
    print(saida)
    return saida


print(print_full_name(first, last))
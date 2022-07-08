string = 'abracadabra'
position = 5
character = 'k'

def mutate_string(string, position, character):

    return string[:position]+character+string[position+1:]

print(mutate_string(string, position, character))

"""
cara = 'y'
nome = 'pablo'

nome1 = nome[3]

print(nome1)

nome2 = nome[:3]+cara+nome[3+1:]

print(nome2)

"""
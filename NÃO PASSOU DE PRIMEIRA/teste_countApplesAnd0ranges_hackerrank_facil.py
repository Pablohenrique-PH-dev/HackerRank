import random

"""   GERADOR AUTOMÁTICO DE VARIÁVEIS DE MAÇÃS E LARANJAS   """

###############   PRIMEIRA MANEIRA QUE FIZ  ###############
  #- GERAÇÃO MANUAL DE VARIÁVEIS PARA LISTAS DE FRUTAS

macas = [2, 3, -4]
laranjas = [3, -2, -1]


"""
7 11
5 15
3 2
-2 2 1
5 -6

###############   SEGUNDA MANEIRA QUE FIZ   ###############
    - GERAÇÃO AUTOMÁTICA DE VARIÁVEIS PARA LISTAS DE FRUTAS FOR IN RANGE 

n_de_frutas = 5
 
macas = []  lista de itens de maçã

for n in range(n_de_frutas):
    num = random.randint(-5, 5)
    macas.append(num)
    
laranjas = [] 

for n in range(n_de_frutas):
    num = random.randint(-5,5)
    laranjas.append(num)
"""
################     TERCEIRA MANEIRA QUE FIZ       #############
#        - GERAÇÃO AUTOMÁTICA DE VARIÁVEIS PARA LISTAS DE FRUTAS FOR IN RANGE UTILIZANDO List Comprehension
'''
n_de_frutas = 3

macas = [random.randint(-5, 5) for m in range(n_de_frutas)]   # Gerador de numeros aleatórios de maçãs

laranjas = [random.randint(-5, 5) for l in range(n_de_frutas)]  # Gerador de numeros aleatórios de laranja

print('\nPosições que as Maçãs cairam: \n\n Posição da 1º foi: {} \n Posição da 2º foi: {} \n Posição da 3º foi: {}'
      .format(macas[0], macas[1], macas[2]))

print('-'* 40)

print('Posições que as laranjas cairam: \n\n Posição da 1º foi: {} \n Posição da 2º foi: {} \n Posição da 3º foi: {}'
      .format(laranjas[0], laranjas[1], laranjas[2]))
'''
##############   POSIÇÕES DOS OBJETOS NO PROBLEMA    ##################

s = 7     #inicio da casa
t = 10    #final da casa
a = 4     #posição da macieira
b = 12    #posição da laranjeira

##############   FUNÇÃO    ##################

def countApplesAndOranges(s, t, a, b, macas, laranjas):
    mac = 0
    for maca in macas:
        if maca + a >= s and maca + a <= t:
            mac += 1

    laran = 0
    for laranja in laranjas:
        if laranja + b >= s and laranja + b <= t:
            laran += 1

    #print(mac)
    #print(laran)
    return mac, laran

print(countApplesAndOranges(s, t, a, b, macas, laranjas))
frutas = countApplesAndOranges(s, t, a, b, macas, laranjas)



print('-'* 40)

print('Na casa de Sam caiu as seguintes quantidades de frutas: \n\n {} maçãs \n {} laranjas'.format(frutas[0], frutas[1]))

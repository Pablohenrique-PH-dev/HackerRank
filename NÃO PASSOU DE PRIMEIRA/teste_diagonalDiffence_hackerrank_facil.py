import  random

"""
###############   PRIMEIRA MANEIRA QUE FIZ  ###############

 - GERAÇÃO MANUAL DE VARIÁVEIS PARA MATRIZ QUADRADA

test1 = [[1, 2, 3], [4, 2, 6], [9, 8, 9]]
test2 = [[4, 9, 7], [9, 2, 3], [1, 9, 7]]
test3= [[7, 9, 2], [9, 9, 3], [1, 9, 7]]
list4 = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

"""
"""
###############   SEGUNDA MANEIRA QUE FIZ  ###############
        
 - GERAÇÃO AUTOMÁTICA DE VARIÁVEIS PARA MATRIZ QUADRADA COM FOR IN RANGE
                                          
n_linhas = 3
n_colunas = 3

matriz = []

for i in range(n_linhas):
    linha = []
    for j in range(n_colunas):
        num = random.randint(-99,100)
        linha.append(num)
    matriz.append(linha)

print(matriz)
"""
################     TERCEIRA MANEIRA QUE FIZ       #############

#  - GERAÇÃO AUTOMÁTICA DE VARIÁVEIS PARA MATRIZ QUADRADA COM FOR IN RANGE UTILIZANDO List Comprehension

n_linhas = 3
n_colunas = 3

matriz = [[random.randint(-99,100) for j in range(n_colunas)] for i in range(n_linhas)]



def diagonalDiffence(arr):
    soma_esq_para_dir =  arr[0][0] + arr[1][1] + arr[2][2]
    soma_dir_para_esq =  arr[0][2] + arr[1][1] + arr[2][0]
    diferenca = soma_esq_para_dir - soma_dir_para_esq
    if diferenca > 0:
        difer = diferenca * 1
    elif diferenca < 0:
        difer = diferenca * -1
    else:
        difer = 0

    return difer


print(' \nresultado da diferença é {} e sua matriz: \n\n{} \n{} \n{}'.format(diagonalDiffence(matriz), matriz[0], matriz[1], matriz[2]))



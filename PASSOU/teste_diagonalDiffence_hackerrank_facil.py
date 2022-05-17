# diagonalDiffence_hackerrank_facil

# Elaboração do raciocínio

"""           Explicação da lista_2d

lista_2d = 'i' é a linha da matriz ou index da lista dentro da outra lista_2d
           'j' é a coluna da matriz ou index do item de dentro da lista 'i' em lista_2d


list_2d[i][j]

           j 0  1  2       i                    j  0  1  2      j  0  1  2     j  0  1  2
             #  #  #
list_2d = [ [1, 2, 3],   # 0       list_2d = [i#0 [1, 2, 3], i#1 [4, 5, 6], i#2 [7, 8, 9] ]
            [4, 5, 6],   # 1
            [7, 8, 9] ]  # 2


"""

"""    # Código de elaboração 



#          j 0  1  2       i
list_2d = [ [1, 2, 3],   # 0
            [4, 5, 6],   # 1
            [7, 8, 9] ]  # 2

# list of lists.
# em uma matriz ----    i = linha # j = coluna
i,j = 0,0

while(i < len(list_2d)):
    print(list_2d[i][j])
    i += 1
    j += 1


i = 0
j = len(list_2d) -1

while(i < len(list_2d)):
    print(list_2d[i][j])
    i += 1
    j -= 1

"""



def diagonalDifference(arr):
    leftDiagonalSum, rightDiagonalSum = 0, 0
    arr_len = len(arr)
    i = 0
    j = 0

    while( i < arr_len):
        leftDiagonalSum += arr[i][j]
        i += 1
        j += 1

    i = 0
    j = arr_len -1

    while( i < arr_len):
        rightDiagonalSum += arr[i][j]
        i += 1
        j -= 1

    return abs(leftDiagonalSum - rightDiagonalSum)


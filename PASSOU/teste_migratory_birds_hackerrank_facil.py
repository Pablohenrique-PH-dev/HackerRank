# teste_migratory_birds_hackerrank_facil

arr = [1, 4, 4, 4, 5, 3]
#arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 7, 7, 7]


list_sem_num_repetido = []

for num in arr:
    list_sem_num_repetido.append(num)
    list_sem_num_repetido = set(list_sem_num_repetido)
    list_sem_num_repetido = list(list_sem_num_repetido)

lista_quant_num_repetidos = []
for item in list_sem_num_repetido:
    quantos_num = arr.count(item)
    lista_quant_num_repetidos.append(quantos_num)
    #print(quantos_num)

x = 0
for maior_repeticao in lista_quant_num_repetidos:
    if maior_repeticao > x:
        x = maior_repeticao
        i = lista_quant_num_repetidos.index(maior_repeticao)


#print(lista_de_test)
#print(lista_quant_num_repetidos)
print(list_sem_num_repetido[i])

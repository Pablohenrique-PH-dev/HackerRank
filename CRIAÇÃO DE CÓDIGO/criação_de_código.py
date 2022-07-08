array_1 = [150, 179, 149, 152, 154]

array_2 = [162, 181, 151, 160, 170]

def ordem_de_altura_entre_filas_para_foto(list_1, list_2):
    if len(list_1) >= 2 and len(list_2) >= 2:
        if len(list_1) == len(list_2):
            list_test = []
            for i, num in enumerate(list_1):
                if num < list_2[i]:
                    list_test.append(num)

    if len(list_test) < len(list_2):
        return False
    return True


print(ordem_de_altura_entre_filas_para_foto(array_1, array_2))


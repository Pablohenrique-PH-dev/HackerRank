string = "BBBBBBBBBBBBBAACCCDD"
list = []

for i in range(1):
    for p in string:
        print(p)



for l in string:
    test = l
    if l == test:
        letras = string.count(l)
        list.append(l)

    #print(letras, l)

#print(list)


list1 = []
test1 = 'z'
for c in string:
    if c != test1:
        test1 = c

        list1.append(c)

list_final = []
for a, b in enumerate(list1):
    letras1 = list.count(list1[a])
    list_final.append((letras1,b))
    print(letras1,b)

print(list_final)

'''
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

'''
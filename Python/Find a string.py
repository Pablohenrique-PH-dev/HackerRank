string = 'ABCDCDC'
sub_string = 'CDC'

def count_substring(string, sub_string):
    lista = []
    n = 0
    x = 0

    for l in string:
        lista.append(l)
        if len(lista) == len(sub_string):
            #print(lista)
            string_teste = ''.join(lista)
            #print(string_teste)
            n += 1
            lista.pop(0)
            if string_teste == sub_string:
                x += 1
    #print(x)
    return x

print(count_substring(string, sub_string))

#print(lista)
#print(n)

#print(len(string2))


#string = string1.count('CDC')
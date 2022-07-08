"""

Escreva uma função que recebe uma string não vazia e a com prima de forma a
substituir as sequências de caracteres iguais por um contador seguido do caractere em si,
por exemplo "AAA" deve ser codificada como "3A", "AABBB" Como "2A3B" e assim por
diante.
para complicarmos um pouco a string de entrada pode conter qualquer caractere,
incluindo números e caracteres especiais. E já as estringues codificadas deve ser
decodificáveis, nos não podemos ingenuamente codificar uma string longa simplesmente
pela repetição por exemplo "AAAAAAAAAAAA" (12 A's) não poderia ser
codificado como "12A"  uma vez que uma string poderia ser decodificada tanto como
"AAAAAAAAAAAA" quanto "1AA". logo, a repetição de 10 ou mais caracteres, deveM ser
codificada de forma dividida, ou seja, por exemplo acima deveria ser codificada como
"9A3A".


    exemplo de entrada

    string = "BBBBBBBBBBBBBAACCCDD"


    exemplo de saida:
    "9B4B2A3C2D"

"""

string = "BBBBBBBBBBBBBAACCCDD"


def repeticao_de_letras_na_string(string):
    lista = []
    teste = ''

    for letra in string:
        if letra != teste:
            teste = letra
            tamanho_teste = string.count(letra)
            if tamanho_teste > 9:
                lista.append("{}{}".format(tamanho_teste - tamanho_teste + 9, letra))
                lista.append("{}{}".format(tamanho_teste - 9, letra))
            else:
                lista.append("{}{}".format(tamanho_teste, letra))

    saida = ''.join(lista)
    return saida


print(repeticao_de_letras_na_string(string))


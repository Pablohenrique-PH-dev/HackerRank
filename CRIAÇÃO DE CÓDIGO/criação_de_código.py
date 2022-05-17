def pageCount(n, p):

    teste_livro_e_impar_ou_par = n % 2

    valores = []

    inicio_do_livro = p / 2
    valores.append(inicio_do_livro)

    if teste_livro_e_impar_ou_par == 0:
        fim_do_livro = (n - p) / 2 + 0.5
        valores.append(fim_do_livro)

        resultado = int(min(valores))

        return resultado

    if teste_livro_e_impar_ou_par == 1:
        fim_do_livro = (n - p) / 2
        valores.append(fim_do_livro)

        resultado = int(min(valores))

        return resultado

print(pageCount(11, 6))

"""

n = 11  # Páginas do livro
p = 6   # Página escolhida

def pageCount(n, p):

    teste_livro_e_impar_ou_par = n % 2    # Verifica se o total de Páginas do livro são ímpar ou par

    valores = []    # Armazena os valores de numeros de paginas da frente e de tras do livro até a página escolhida

    # Realiza o calculo do numero de pàginas do inicio até a página escolhida
    inicio_do_livro = p / 2
    valores.append(inicio_do_livro)
# ---------------------------------------------------------------------------

    if teste_livro_e_impar_ou_par == 0:
        fim_do_livro = (n - p) / 2 + 0.5
        valores.append(fim_do_livro)

        resultado = int(min(valores))
        #print(valores)
        #print(resultado)

        return resultado

    if teste_livro_e_impar_ou_par == 1:
        fim_do_livro = (n - p) / 2
        valores.append(fim_do_livro)

        resultado = int(min(valores))
        #print(valores)
        #print(resultado)

        return resultado

print(pageCount(11, 6))

"""
"""
n = 10
p = 10

meio_do_livro = n / 2

teste_total_pag_do_livro_é_impar_ou_par = n % 2

teste_pag_do_livro_selecionada_é_impar_ou_par = p % 2

teste_penultima_pag = p + 1


# condição para livro com numero de paginas pares

if teste_total_pag_do_livro_é_impar_ou_par == 0:
    meio_do_livro = int(meio_do_livro)
    m1 = meio_do_livro      #frente_do_livro
    m2 = meio_do_livro + 1   #atras_do_livro
    print(m1, m2)
    if p <= m1:
        if teste_pag_do_livro_selecionada_é_impar_ou_par == 0:
            folhas_viradas = p / 2
            print(folhas_viradas)
        if teste_pag_do_livro_selecionada_é_impar_ou_par == 1:
            folhas_viradas = p / 2
            folhas_viradas = int(folhas_viradas)
            print(folhas_viradas)
    if p >= m2:
        if teste_pag_do_livro_selecionada_é_impar_ou_par == 0 and p != n:
            folhas_viradas = (n - p) / 2
            print(folhas_viradas)
        if teste_pag_do_livro_selecionada_é_impar_ou_par == 1 and p != n - 1:
                folhas_viradas = ((n - p) / 2 ) + 1
                folhas_viradas = int(folhas_viradas)
                #folhas_viradas = ((n - p) - 1)/ 2
                print(folhas_viradas)
        if p == n - 1:
            folhas_viradas = n - p
            print(folhas_viradas)
        if teste_pag_do_livro_selecionada_é_impar_ou_par == 0:
            if teste_penultima_pag - 1 == n:
                folhas_viradas = (n - p)
                print(folhas_viradas)
        #if
         #   folhas_viradas = n - p
            #print(folhas_viradas)


"""

"""
numero_de_paginas = 8
pagina = 2
primeira_pagina = 1

meio_do_livro = numero_de_paginas // 2
x = numero_de_paginas - pagina
v = x // 2

a = numero_de_paginas - pagina
b = pagina - primeira_pagina
r = pagina % 2
print(r)

if pagina == numero_de_paginas or primeira_pagina:
    n_p0 = 0
    print(n_p0)
if b < a and b != 0:
   if r == 1:
       n_p = (pagina // 2)
       print(n_p)
   else:
       n_p = (pagina // 2)
       print(n_p)
if b > a and a != 0:
    if r == 1:
        n_p1 = (pagina // 2) - 2
        print(n_p1)
    else:
        n_p1 = (pagina // 2) - 2
        print(n_p1)


#print(x)
#print(v)
#print(meio_do_livro)
#print(a)
#print(b)
"""
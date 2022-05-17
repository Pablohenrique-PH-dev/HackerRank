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
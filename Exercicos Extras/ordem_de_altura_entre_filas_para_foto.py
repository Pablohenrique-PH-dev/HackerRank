"""

É o dia da foto da turma em uma escola local e você foi o fotógrafo escolhido para
tirá-las. A classe que você irá fotografar tem um número par de alunos e todos esses
alunos estão usando uniformes pretos ou laranjas em iguais quantidades, ou seja,
metade da turma está com uniformes preto e metade com uniforme de laranja. Você é
responsável por arranjar os alunos em duas filas para fotografar, uma na frente da
outra. Cada fila deve conter o mesmo número de alunos e deve preencher os seguintes
requisitos:

 - todos os alunos usando uniformes pretos deve estar na mesma fila
 - todos os alunos usando uniforme laranja deve estar na mesma fila
 - todos os alunos na fila de trás devem ser estritamente mais alto que os aluno
   diretamente na fila da frente.

você receberá 2 arrays de entrada um contendo a altura dos alunos com uniformes
 preto e outro contendo a altura dos alunos com uniforme laranja. esses arrays sempre
 terão o mesmo tamanho e cada altura em centímetro será um inteiro positivo. Escreva uma
 função que retorne true ou false Caso seja possível ou não tira a foto de uma
 determinada turma seguindo os parâmetros estabelecida. você assumirá que cada
 turma tem ao menos dois alunos.

  exemplo de entrada:

    array_1 = [150, 179, 149, 152, 154]

    array_2 = [162, 181, 151, 160, 170]


  exemplo de saida:

    true

"""


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
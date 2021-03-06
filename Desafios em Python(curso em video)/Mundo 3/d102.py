#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """

    :param num: Recebe o numero que será calculado o fatorial
    :param show: Parametro opcional, mostra a conta na tela
    :return: Retorna o valor do fatorial de num
    """
    fat = 1
    for i in range (num, 0, -1):

        if show :
            print(i, end=" ")
            if i > 1:
                print(" X ", end=" ")
            else:
                print(" = ", end=" ")
        fat *= i
    print(fat)
help(fatorial)
n = int(input("Informe um números: "))

fatorial(n, show=True)

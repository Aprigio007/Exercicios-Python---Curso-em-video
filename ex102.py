def fatorial(n, show=False):
    """
    Calcula o fatorial de um número inteiro não negativo e retorna o resultado.
    O parâmetro opcional 'show' (padrão False) indica se o processo de cálculo do fatorial deve ser mostrado na tela.

    :param n: int
        O número inteiro não negativo cujo fatorial deve ser calculado.
    :param show: bool, opcional
        Indica se o processo de cálculo do fatorial deve ser mostrado na tela. O valor padrão é False.
    :return: int
        O resultado do cálculo do fatorial de n.
    """
    soma = n
    for c in range(n - 1, 0, -1):
        soma = soma * c
    if show == True:
        for c in range(n, 0, -1):
            if c == 1:
                print(f'{1} ==', end=' ')
            else:
                print(f'{c} x', end=' ')
    else:
        return soma
    return soma

print(fatorial(5, show=False))
def cor(numero_cor=10, cor=''):
    """
    :param numero_cor: Color separate into a numbers
    :param cor: command used to set color with "cor.cor(cor='vermelho') for example
    :return: Code to simplify the use of colors.
    """
    if numero_cor == 0:
        return '\033[m'  # 0 Sem cor
    elif numero_cor == 1:
        return '\033[1;31m'  # 1 Vermelho
    elif numero_cor == 2:
        return '\033[1;32m'  # 2 Verde
    elif numero_cor == 3:
        return '\033[1;33m'  # 3 Amarelo
    elif numero_cor == 4:
        return '\033[1;34m'  # 4 Azul
    elif numero_cor == 5:
        return '\033[1;35m'  # 5 Roxo
    elif numero_cor == 6:
        return '\033[1;30m'  # 6 Preto
    elif 'APAGA' in cor.strip().upper():
        return '\033[m'
    elif 'VERMELHO' in cor.strip().upper():
        return '\033[1;31m'
    elif 'VERDE' in cor.strip().upper():
        return '\033[1;32m'
    elif 'AMARELO' in cor.strip().upper():
        return '\033[1;33m'
    elif 'AZUL' in cor.strip().upper():
        return '\033[1;34m'
    elif 'ROXO' in cor.strip().upper():
        return '\033[1;35m'
    elif 'PRETO' in cor.strip().upper():
        return '\033[1;30m'
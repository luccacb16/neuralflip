import numpy as np

def F38(seq: str) -> float:
    '''
    F38: Desvio padrão do tamanho das sequências 
    
    Args:
        seq (str): sequência

    Returns:
        float: desvio padrão do tamanho das sequências
    '''
    comprimentos = []
    contador = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            contador += 1
        else:
            comprimentos.append(contador)
            contador = 1

    comprimentos.append(contador)

    return np.std(comprimentos) if comprimentos else 0.0
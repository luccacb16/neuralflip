import numpy as np

def F37(seq: str) -> float:
    '''
    Feature 37: Desvio padrão do tamanho das sequências de 1s

    Args: 
        seq (str): sequência

    Returns:
        float: desvio padrão do tamanho das sequências de 1s
    '''
    sequencias_zeros = seq.split('0')
    
    comprimentos = [len(s) for s in sequencias_zeros if s]

    return np.std(comprimentos) if comprimentos else 0.0
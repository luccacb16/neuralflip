import numpy as np

def F37(seq: str) -> float:
    '''
    Feature 36: Desvio padrão do tamanho das sequências de 0s

    Args: 
        seq (str): sequência

    Returns:
        float: desvio padrão do tamanho das sequências de 0s
    '''
    sequencias_zeros = seq.split('1')
    
    comprimentos = [len(s) for s in sequencias_zeros if s]

    return np.std(comprimentos) if comprimentos else 0.0
import numpy as np

def F24(seq1: str, seq2: str) -> float:
    '''
    F24: calcular distância euclidiana entre duas sequências
    '''
    array1 = np.array([int(bit) for bit in seq1])
    array2 = np.array([int(bit) for bit in seq2])

    return np.linalg.norm(array1 - array2)
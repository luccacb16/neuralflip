from scipy.stats import kurtosis
from collections import Counter

def F33(seq: str) -> int:
    '''
    Feature 33: Complexidade de Permutação

    Função que calcula a complexidade de permutação da sequência.

    Args:
        seq (str): sequência

    Returns:
        float: valor complexidade de permutação da sequência
    '''

    sorted_indices = sorted(range(len(seq)), key=lambda k: seq[k])

    complexity = 0
    visited = [False] * len(seq)

    for i in range(len(seq)):
        if visited[i] or sorted_indices[i] == i:
            continue

        j = i
        while not visited[j]:
            visited[j] = True
            j = sorted_indices[j]
            complexity += 1

    return complexity
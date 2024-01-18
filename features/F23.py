import math
from collections import Counter

def F23(seq: str) -> float:
    '''
    Feature 23: Entropia Mínima Normalizada
    
    Função que retorna a entropia mínima esperada da distribuição de probabilidade,
    sendo normalizada pelo comprimento da sequência
    
    Args: 
        seq (str): sequência
        
    Returns:
        float: Entropia Mínima Normalizada
    '''
    
    char_freq = Counter(seq)
    prob_dist = {char : count / len(seq) for char, count in char_freq.items()}
    
    if len(prob_dist) == 1:
        return 0

    # Calcula a Entropia Mínima Normalizada
    min_entropy = min(-math.log2(prob) for prob in prob_dist.values())
    normalized_min_entropy = min_entropy / math.log2(len(prob_dist))

    return normalized_min_entropy
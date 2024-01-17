from collections import Counter
import math

def F35(seq) -> float:
    '''
    Feature 35: Complexidade de Entropia Condicional

    Função que calcula a complexidade de entropia condicional da sequência com janelas de tamanho 5.

    Args:
        seq (str): sequência

    Returns:
        float: valor da complexidade de entropia condicional da sequência 
    '''
    
    # Tamanho das janelas deslizantes
    window_size = 5

    windows = [seq[i:i+window_size] for i in range(len(seq)-window_size+1)]

    window_counts = Counter(windows)

    window_probabilities = {window: count / len(windows) for window, count in window_counts.items()}

    conditional_entropy = -sum(prob * math.log2(prob) for prob in window_probabilities.values())

    return conditional_entropy
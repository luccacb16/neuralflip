from collections import Counter

def F34(seq) -> int:
    '''
    Feature 34: Complexidade de Espectral

    Função que calcula a complexidade de espectral da sequência com padrões de tamanho 5.

    Args:
        seq (str): sequência

    Returns:
        int: valor complexidade de espectral da sequência 
    '''

    # Tamanho dos padrões a serem considerados
    default_length = 5

    pattern = [seq[i:i+default_length] for i in range(len(seq)-default_length+1)]

    pattern_frequency = Counter(pattern)

    spectral_complexity = len(pattern_frequency)

    return spectral_complexity
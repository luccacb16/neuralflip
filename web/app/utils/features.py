from collections import Counter
from scipy.stats import skew, kurtosis
import numpy as np
import math
import zlib

def F1(seq: str) -> int:
    '''
    Feature 1: Caractere mais frequente
    
    Função que retorna o caractere mais frequente (0 ou 1) ou -1 se a frequência for igual
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: -1, 0 ou 1
    '''
    
    return -1 if seq.count('0') == seq.count('1') else int(max('01', key=seq.count))

def F2(seq: str) -> int:
    '''
    Feature 2: Quantidade de 0s
    
    Função que retorna a quantidade de 0s
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: quantidade de 0s
    '''
    
    return int(seq.count('0'))

def F3(seq: str) -> int:
    '''
    Feature 3: Quantidade de 1s
    
    Função que retorna a quantidade de 1s
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: quantidade de 1s
    '''
    
    return int(seq.count('1'))

def F4(seq: str) -> int:
    '''
    Feature 4: Maior sequência de 0s
    
    Função que retorna a maior sequência de 0s
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: maior sequência de 0s
    '''
    
    return max([len(i) for i in seq.split('1')])
def F5(seq: str) -> int:
    '''
    Feature 5: Maior sequência de 1s
    
    Função que retorna a maior sequência de 1s
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: maior sequência de 1s
    '''
    
    return max([len(i) for i in seq.split('0')])
def F6(seq: str) -> int:
    '''
    Feature 6: Número de transições entre 0 e 1
    
    Função que retorna o número de transições entre 0 e 1
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: número de transições entre 0 e 1
    '''
    
    return seq.count('01') + seq.count('10')
def F7(seq: str) -> float:
    '''
    Feature 7: Tamanho médio das sequências de 0s
    
    Função que retorna o tamanho médio das sequências de 0s
    
    Args: 
        seq (str): sequência
        
    Returns:
        float: tamanho médio das sequências de 0s
    '''
    
    seqs = [s for s in seq.split('1') if s]
    return sum(len(s) for s in seqs) / len(seqs) if seqs else 0
def F8(seq: str) -> float:
    '''
    Feature 8: Tamanho médio das sequências de 1s
    
    Função que retorna o tamanho médio das sequências de 1s
    
    Args: 
        seq (str): sequência
        
    Returns:
        float: tamanho médio das sequências de 1s
    '''
    
    seqs = [s for s in seq.split('0') if s]
    return sum(len(s) for s in seqs) / len(seqs) if seqs else 0
def F9(seq: str) -> int:
    '''
    Feature 9: Frequência de 10101
    
    Função que retorna a frequência de 10101
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: frequência de 10101
    '''
    
    return seq.count('10101')
def F10(seq: str) -> int:
    '''
    Feature 10: Frequência de 11111
    
    Função que retorna a frequência de 11111
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: frequência de 11111
    '''
    
    return seq.count('11111')
def F11(seq: str) -> int:
    '''
    Feature 11: Quantidade de caracteres isolados
    
    Função que retorna a quantidade de caracteres isolados
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: quantidade de caracteres isolados
    '''
    
    seqs_0 = [s for s in seq.split('1') if s]
    seqs_1 = [s for s in seq.split('0') if s]
    return seqs_0.count('0') + seqs_1.count('1')
def F12(seq: str) -> int:
    '''
    Feature 12: Diferença entre maior sequência de 0s e 1s
    
    Função que retorna a diferença entre maior sequência de 0s e 1s
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: diferença entre maior sequência de 0s e 1s
    '''
    
    maior_seq_0 = max([s for s in seq.split('1') if s], key=len, 
default='')
    maior_seq_1 = max([s for s in seq.split('0') if s], key=len, 
default='')
    return abs(len(maior_seq_0) - len(maior_seq_1))
def F13(seq: str) -> int:
    '''
    Feature 13: Quantidade de sequências de 0s
    
    Função que retorna a quantidade de sequências de 0s
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: quantidade de sequências de 0s
    '''
    
    seqs_0 = [s for s in seq.split('1') if s]
    return len(seqs_0)
def F14(seq: str) -> int:
    '''
    Feature 13: Quantidade de sequências de 1s
    
    Função que retorna a quantidade de sequências de 1s
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: quantidade de sequências de 1s
    '''
    
    seqs_1 = [s for s in seq.split('0') if s]
    return len(seqs_1)
def F15(seq: str) -> int:
    '''
    Feature 15: Complexidade de Lempel-Ziv
    
    Função que retorna a complexidade de Lempel-Ziv da sequência.
    Esta medida reflete a quantidade e a variedade de padrões na sequência.
    
    Args: 
        seq (str): sequência de caracteres '0' e '1'.
        
    Returns:
        int: valor da complexidade de Lempel-Ziv.
    '''

    n = len(seq)
    i, complexidade_lz = 0, 0
    substrings = set()

    while i < n:
        nova_substring = ''
        while i < n and (nova_substring in substrings or nova_substring == ''):
            nova_substring += seq[i]
            i += 1
        substrings.add(nova_substring)
        complexidade_lz += 1

    return complexidade_lz

def F16(seq: str) -> float:
    '''
    Feature 16: Entropia de Shannon da Sequência

    Função que retorna a entropia de Shannon da sequência de 0s e 1s.
    A entropia é uma medida da incerteza ou aleatoriedade da sequência.

    Args: 
        seq (str): sequência de caracteres '0' e '1'.
        
    Returns:
        float: valor da entropia de Shannon.
    '''
    
    prob_0 = seq.count('0') / len(seq)
    prob_1 = seq.count('1') / len(seq)

    # Evita o logaritmo de zero adicionando um pequeno valor epsilon se prob_0 ou prob_1 for zero
    epsilon = 1e-10
    entropia = 0
    if prob_0 > 0:
        entropia -= prob_0 * math.log2(prob_0 + epsilon)
    if prob_1 > 0:
        entropia -= prob_1 * math.log2(prob_1 + epsilon)

    return entropia


def F17(seq: str) -> float:
    '''
    Feature 39: Desvio padrão da frequência das runs
    
    Args:
        seq (str): sequência
        
    Returns:
        float: desvio padrão da frequência das runs
    '''
    runs = []
    current_run = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1
    runs.append(current_run)

    run_counts = Counter(runs)
    freq_runs = [run_counts[i] for i in range(1, 51)]
    
    if len(set(freq_runs)) == 1:
        return 0
        
    return np.std(freq_runs)

def F18(seq: str) -> float:
    '''
    Feature 18: Média da frequência das runs
    
    Args:
        seq (str): sequência
        
    Returns:
        float: média da frequência das runs
    '''
    runs = []
    current_run = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1
    runs.append(current_run)

    run_counts = Counter(runs)
    freq_runs = [run_counts[i] for i in range(1, 51)]
    
    if len(set(freq_runs)) == 1:
        return 0
        
    return np.mean(freq_runs)
def F19(seq: str) -> int:
    '''
    Feature 19: Frequência de '00'
    
    Função que retorna a frequência de '00'
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: frequência de '00'
    '''
    
    tamanho_subseq = 2
    subseqs = [seq[i:i+2] for i in range(len(seq)-1)]
    return subseqs.count('00')
def F20(seq: str) -> int:
    '''
    Feature 19: Frequência de '11'
    
    Função que retorna a frequência de '11'
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: frequência de '11'
    '''
    
    tamanho_subseq = 2
    subseqs = [seq[i:i+2] for i in range(len(seq)-1)]
    return subseqs.count('11')
def F21(seq: str) -> int:
    '''
    Feature 19: Frequência de '01'
    
    Função que retorna a frequência de '01'
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: frequência de '01'
    '''
    
    tamanho_subseq = 2
    subseqs = [seq[i:i+2] for i in range(len(seq)-1)]
    return subseqs.count('01')
def F22(seq: str) -> int:
    '''
    Feature 19: Frequência de '10'
    
    Função que retorna a frequência de '10'
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: frequência de '10'
    '''
    
    tamanho_subseq = 2
    subseqs = [seq[i:i+2] for i in range(len(seq)-1)]
    return subseqs.count('10')

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

def F24(seq: str) -> float:
    '''
    Feature 24: Desvio padrão do tamanho das sequências de 0s

    Args: 
        seq (str): sequência

    Returns:
        float: desvio padrão do tamanho das sequências de 0s
    '''
    sequencias_zeros = seq.split('1')
    
    comprimentos = [len(s) for s in sequencias_zeros if s]

    return np.std(comprimentos) if comprimentos else 0.0

def F25(seq: str) -> float:
    '''
    Feature 25: Desvio padrão do tamanho das sequências de 1s

    Args: 
        seq (str): sequência

    Returns:
        float: desvio padrão do tamanho das sequências de 1s
    '''
    sequencias_zeros = seq.split('0')
    
    comprimentos = [len(s) for s in sequencias_zeros if s]

    return np.std(comprimentos) if comprimentos else 0.0

def F26(seq: str) -> float:
    '''
    F26: Desvio padrão do tamanho das sequências 
    
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

def F27(seq: str) -> float:
    '''
    Feature 27: Skewness do Comprimento dos Runs

    FUnção que calcula a skewness (assimetria) da distribuição do comprimento dos runs (sequências contínuas de 0s ou 1s) na sequência.

    Args:
        seq (str): sequência binária

    Returns:
        float: valor de Skewness para a distribuição do comprimento dos runs
    '''

    runs = []
    current_run = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1

    runs.append(current_run)
    
    if len(set(runs)) == 1:
        return 0

    return skew(runs)

def F28(seq: str) -> float:
    '''
    Feature 28: Skewness da Distribuição de Frequências de Runs

    Função que calcula a skewness (assimetria) da distribuição de frequências dos comprimentos de runs na sequência.

    Args:
        seq (str): sequência

    Returns:
        float: valor de Skewness para a distribuição de frequências dos comprimentos dos runs
    '''

    runs = []
    current_run = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1
    runs.append(current_run)

    # Contagem de frequência dos runs de tamanhos 1 a 50
    run_counts = Counter(runs)
    freq_runs = [run_counts[i] for i in range(1, 51)]
    
    if len(set(freq_runs)) == 1:
        return 0

    return skew(freq_runs)

def F29(seq: str) -> float:
    '''
    Feature 29: Kurtosis da Distribuição de Runs

    Função que calcula a curtose da distribuição do comprimento dos runs (sequências contínuas de 0s ou 1s) na sequência.

    Args:
        seq (str): sequência

    Returns:
        float: valor de Kurtosis para a distribuição do comprimento dos runs
    '''

    runs = []
    current_run = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1

    runs.append(current_run)
    
    if len(set(runs)) == 1:
        return 0

    return kurtosis(runs, fisher=False)

def F30(seq: str) -> float:
    '''
    Feature 30: Kurtosis da Distribuição de Frequências de Runs

    Função que calcula a curtose da distribuição de frequências dos comprimentos de runs na sequência.

    Args:
        seq (str): sequência

    Returns:
        float: valor de Kurtosis para a distribuição de frequências dos comprimentos dos runs
    '''

    runs = []
    current_run = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1
    runs.append(current_run)

    run_counts = Counter(runs)
    freq_runs = [run_counts[i] for i in range(1, 51)]
    
    if len(set(freq_runs)) == 1:
        return 0

    return kurtosis(freq_runs, fisher=False)
def F31(seq: str) -> float:
    '''
    Feature 31: Proporção de 0s e 1s em posições pares e ímpares

    Função que calcula uma métrica combinada que representa a proporção de 0s e 1s em posições pares e ímpares.
    
    proporcao = ((zeros_pares + zeros_impares) - (uns_pares + uns_impares)) / total_chars
    
    Args: 
        seq (str): sequência
        
    Returns:
        float: métrica combinada que representa a proporção de 0s e 1s em posições pares e ímpares.
    '''

    total_chars = len(seq)

    zeros_pares = sum(1 for i, bit in enumerate(seq) if bit == '0' and i % 2 == 0)
    zeros_impares = sum(1 for i, bit in enumerate(seq) if bit == '0' and i % 2 != 0)
    uns_pares = sum(1 for i, bit in enumerate(seq) if bit == '1' and i % 2 == 0)
    uns_impares = sum(1 for i, bit in enumerate(seq) if bit == '1' and i % 2 != 0)
    
    # Calcular a proporção combinada
    proporcao = ((zeros_pares + zeros_impares) - (uns_pares + uns_impares)) / total_chars
    
    return proporcao

def F32(seq: str) -> int:
    '''
    Feature 32: Complexidade de Kolmogorov

    Função que estima a complexidade de Kolmogorov de uma sequência binária. 
    A complexidade é aproximada pelo tamanho da sequência após a compressão com zlib.
    
    Args: 
        seq (str): Sequência
    
    Returns:
        int: tamanho da sequência comprimida, representando a complexidade estimada.
    '''

    comprimido = zlib.compress(seq.encode())

    return len(comprimido)

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

features_list = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10,
                F11, F12, F13, F14, F15, F16, F17, F18, F19, F20,
                F21, F22, F23, F24, F25, F26, F27, F28, F29, F30,
                F31, F32, F33, F34, F35]

selected_features = [F1, F7, F8, F9, F11, F12, F15, F16, F17, F19, F20,
                    F22, F24, F25, F26, F27, F28, F29, F30, F32, F33, F34, F35]

'''
extract_features

Função que recebe a sequência e retorna as features extraídas.

Args:
    - seq (str): sequência
    
Returns:
    - features (list): features extraídas
'''
def extract_features(seq: str) -> list:
    return [f(seq) for f in selected_features]
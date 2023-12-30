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
    
    maior_seq_0 = max([s for s in seq.split('1') if s], key=len, default='')
    maior_seq_1 = max([s for s in seq.split('0') if s], key=len, default='')
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

import math

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

features_list = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F19]

'''
extract_features

Função que recebe a sequência e retorna as features extraídas.

Args:
    - seq (str): sequência
    
Returns:
    - features (list): features extraídas
'''
def extract_features(seq: str) -> list:
    return [f(seq) for f in features_list]
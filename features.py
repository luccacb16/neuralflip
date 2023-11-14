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
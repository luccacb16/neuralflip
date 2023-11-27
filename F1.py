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
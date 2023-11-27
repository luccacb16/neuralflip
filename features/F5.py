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
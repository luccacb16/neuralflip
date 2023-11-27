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
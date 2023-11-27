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
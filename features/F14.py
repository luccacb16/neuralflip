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
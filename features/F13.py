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
    print(len(seqs_0))
    return len(seqs_0)
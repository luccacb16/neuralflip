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
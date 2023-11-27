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
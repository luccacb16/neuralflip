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
def F11(seq: str) -> int:
    '''
    Feature 11: Quantidade de caracteres isolados
    
    Função que retorna a quantidade de caracteres isolados
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: quantidade de caracteres isolados
    '''
    
    seqs_0 = [s for s in seq.split('1') if s]
    seqs_1 = [s for s in seq.split('0') if s]
    return seqs_0.count('0') + seqs_1.count('1')
def F22(seq: str) -> int:
    '''
    Feature 19: Frequência de '10'
    
    Função que retorna a frequência de '10'
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: frequência de '10'
    '''
    
    tamanho_subseq = 2
    subseqs = [seq[i:i+2] for i in range(len(seq)-1)]
    return subseqs.count('10')
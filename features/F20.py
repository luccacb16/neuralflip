def F20(seq: str) -> int:
    '''
    Feature 19: Frequência de '11'
    
    Função que retorna a frequência de '11'
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: frequência de '11'
    '''
    
    tamanho_subseq = 2
    subseqs = [seq[i:i+2] for i in range(len(seq)-1)]
    return subseqs.count('11')
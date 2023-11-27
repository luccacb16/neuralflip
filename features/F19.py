def F19(seq: str) -> int:
    '''
    Feature 19: Frequência de '00'
    
    Função que retorna a frequência de '00'
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: frequência de '00'
    '''
    
    tamanho_subseq = 2
    subseqs = [seq[i:i+2] for i in range(len(seq)-1)]
    return subseqs.count('00')
def F21(seq: str) -> int:
    '''
    Feature 19: Frequência de '01'
    
    Função que retorna a frequência de '01'
    
    Args: 
        seq (str): sequência
        
    Returns:
        int: frequência de '01'
    '''
    
    tamanho_subseq = 2
    subseqs = [seq[i:i+2] for i in range(len(seq)-1)]
    return subseqs.count('01')
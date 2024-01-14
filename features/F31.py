def F31(seq: str) -> float:
    '''
    Feature 31: Proporção de 0s e 1s em posições pares e ímpares

    Função que calcula uma métrica combinada que representa a proporção de 0s e 1s em posições pares e ímpares.
    
    proporcao = ((zeros_pares + zeros_impares) - (uns_pares + uns_impares)) / total_chars
    
    Args: 
        seq (str): sequência
        
    Returns:
        float: métrica combinada que representa a proporção de 0s e 1s em posições pares e ímpares.
    '''

    total_chars = len(seq)

    zeros_pares = sum(1 for i, bit in enumerate(seq) if bit == '0' and i % 2 == 0)
    zeros_impares = sum(1 for i, bit in enumerate(seq) if bit == '0' and i % 2 != 0)
    uns_pares = sum(1 for i, bit in enumerate(seq) if bit == '1' and i % 2 == 0)
    uns_impares = sum(1 for i, bit in enumerate(seq) if bit == '1' and i % 2 != 0)
    
    # Calcular a proporção combinada
    proporcao = ((zeros_pares + zeros_impares) - (uns_pares + uns_impares)) / total_chars
    
    return proporcao
def F15(seq: str) -> int:
    '''
    Feature 15: Complexidade de Lempel-Ziv
    
    Função que retorna a complexidade de Lempel-Ziv da sequência.
    Esta medida reflete a quantidade e a variedade de padrões na sequência.
    
    Args: 
        seq (str): sequência de caracteres '0' e '1'.
        
    Returns:
        int: valor da complexidade de Lempel-Ziv.
    '''

    n = len(seq)
    i, complexidade_lz = 0, 0
    substrings = set()

    while i < n:
        nova_substring = ''
        while i < n and (nova_substring in substrings or nova_substring == ''):
            nova_substring += seq[i]
            i += 1
        substrings.add(nova_substring)
        complexidade_lz += 1

    return complexidade_lz
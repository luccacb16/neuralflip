import zlib

def F32(seq: str) -> int:
    '''
    Feature 32: Complexidade de Kolmogorov

    Função que estima a complexidade de Kolmogorov de uma sequência binária. 
    A complexidade é aproximada pelo tamanho da sequência após a compressão com zlib.
    
    Args: 
        seq (str): Sequência
    
    Returns:
        int: tamanho da sequência comprimida, representando a complexidade estimada.
    '''

    comprimido = zlib.compress(seq.encode())

    return len(comprimido)

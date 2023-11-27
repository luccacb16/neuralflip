import math

def F16(seq: str) -> float:
    '''
    Feature 16: Entropia de Shannon da Sequência

    Função que retorna a entropia de Shannon da sequência de 0s e 1s.
    A entropia é uma medida da incerteza ou aleatoriedade da sequência.

    Args: 
        seq (str): sequência de caracteres '0' e '1'.
        
    Returns:
        float: valor da entropia de Shannon.
    '''
    
    prob_0 = seq.count('0') / len(seq)
    prob_1 = seq.count('1') / len(seq)

    # Evita o logaritmo de zero adicionando um pequeno valor epsilon se prob_0 ou prob_1 for zero
    epsilon = 1e-10
    entropia = 0
    if prob_0 > 0:
        entropia -= prob_0 * math.log2(prob_0 + epsilon)
    if prob_1 > 0:
        entropia -= prob_1 * math.log2(prob_1 + epsilon)

    return entropia
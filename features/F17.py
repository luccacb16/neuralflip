import math
import statistics

def F17(seq: str) -> tuple:
    '''
    Feature 17: Desvio padrão das frequencias de sequencias de 0s e 1s

    Função que retorna o desvio padrão do tamanho das frequências de 0s e 1s dentro da sequência

    Args:
        seq (str): sequência

    Returns:
        tuple: desvio padrão do 0 e do 1
    '''
    frequencia_0 = [len(s) for s in seq.split('0') if s]
    media_0 = statistics.mean(frequencia_0)

    frequencia_1 = [len(s) for s in seq.split('1') if s]
    media_1 = statistics.mean(frequencia_1)

    S_0 = 0 if len(frequencia_0) == 1 else math.sqrt(sum((x - media_0)**2 for x in frequencia_0) / (len(frequencia_0) - 1))
    S_1 = 0 if len(frequencia_1) == 1 else math.sqrt(sum((x - media_1)**2 for x in frequencia_1) / (len(frequencia_1) - 1))

    return S_0, S_1




    

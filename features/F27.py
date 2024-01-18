from scipy.stats import skew

def F27(seq: str) -> float:
    '''
    Feature 27: Skewness do Comprimento dos Runs

    FUnção que calcula a skewness (assimetria) da distribuição do comprimento dos runs (sequências contínuas de 0s ou 1s) na sequência.

    Args:
        seq (str): sequência binária

    Returns:
        float: valor de Skewness para a distribuição do comprimento dos runs
    '''

    runs = []
    current_run = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            current_run += 1
        else:
            runs.append(current_run)
            current_run = 1

    runs.append(current_run)
    
    if len(set(runs)) == 1:
        return 0

    return skew(runs)
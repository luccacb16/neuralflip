from scipy.stats import kurtosis

def F29(seq: str) -> float:
    '''
    Feature 29: Kurtosis da Distribuição de Runs

    Função que calcula a curtose da distribuição do comprimento dos runs (sequências contínuas de 0s ou 1s) na sequência.

    Args:
        seq (str): sequência

    Returns:
        float: valor de Kurtosis para a distribuição do comprimento dos runs
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
    print(runs)

    return kurtosis(runs, fisher=False)
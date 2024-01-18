from scipy.stats import kurtosis
from collections import Counter

def F30(seq: str) -> float:
    '''
    Feature 30: Kurtosis da Distribuição de Frequências de Runs

    Função que calcula a curtose da distribuição de frequências dos comprimentos de runs na sequência.

    Args:
        seq (str): sequência

    Returns:
        float: valor de Kurtosis para a distribuição de frequências dos comprimentos dos runs
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

    run_counts = Counter(runs)
    freq_runs = [run_counts[i] for i in range(1, 51)]
    
    if len(set(freq_runs)) == 1:
        return 0

    return kurtosis(freq_runs, fisher=False)
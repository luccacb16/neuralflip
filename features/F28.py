from scipy.stats import skew
from collections import Counter

def F28(seq: str) -> float:
    '''
    Feature 28: Skewness da Distribuição de Frequências de Runs

    Função que calcula a skewness (assimetria) da distribuição de frequências dos comprimentos de runs na sequência.

    Args:
        seq (str): sequência

    Returns:
        float: valor de Skewness para a distribuição de frequências dos comprimentos dos runs
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

    # Contagem de frequência dos runs de tamanhos 1 a 50
    run_counts = Counter(runs)
    freq_runs = [run_counts[i] for i in range(1, 51)]
    
    if len(set(freq_runs)) == 1:
        return 0

    return skew(freq_runs)
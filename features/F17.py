import numpy as np
from collections import Counter

def F17(seq: str) -> float:
    '''
    Feature 39: Desvio padrão da frequência das runs
    
    Args:
        seq (str): sequência
        
    Returns:
        float: desvio padrão da frequência das runs
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
    
    print(freq_runs)
    
    if len(set(freq_runs)) == 1:
        return 0
        
    return np.std(freq_runs)
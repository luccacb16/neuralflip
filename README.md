# NeuralFlip




## Descrição
**Desenvolvido pelo Grupo 3 do Grupo de Processamento e Análise de Dados (PANDA) do Departamento de Computação da UFSCar**

Membros:
- Lucca Couto Barberato
- Matheus Bessa
- Igor Kenji Kawai Ueno
- Luiz Otávio Teixeira Mello
- Evandro Gabriel Vianna Taveira

O projeto NeuralFlip consiste de uma rede neural capaz de classificar uma sequência de 50 caractéres composta de apenas 0s e 1s como gerada por **Humano** ou **Máquina**.

A grande parte dos humanos possui, mesmo que inconscientemente, a crença descrita pela Falácia do Apostador, que diz:

*A falácia do apostador, também conhecida como falácia de Monte Carlo, consiste na crença de que a ocorrência de desvios no comportamento esperado para uma sequência de eventos independentes de algum processo aleatório implica uma maior probabilidade de se obter, em seguida, desvios na direção oposta.*

Esse comportamento pode ser visto em jogos de azar, como roleta, onde um jogador pode acreditar que, após uma sequência de resultados de uma mesma cor, a cor oposta tem maior probabilidade de ocorrer, por isso o nome de falácia do apostador. Esse mesmo comportamento pode ser observado ao tentar gerar uma sequência de lançamentos de moeda (*coin flips*) como na brincadeira Cara ou Coroa. Nós humanos tendemos a acreditar que sequências muito longas de uma mesma face da moeda são menos prováveis de ocorrer, apesar de serem eventos independentes entre si, possuindo a mesma probabilidade.

### **Inspiração**

Inspirados pelo vídeo do canal [MindingTheData](https://www.youtube.com/watch?v=2WiRFLImSvE) *'Are You Good at Being Random? | Attempting to Fake Randomness'*, em que ele cria um classificador para esse problema utilizando uma árvore de decisão, decidimos criar um classificador para esse problema utilizando uma rede neural.

## Dataset

Assim como no vídeo utilizado como referência, realizamos uma coleta pelo [Google Forms](forms.gle/8nFWAZzK9iZLLRHw8) para a obtenção de sequências geradas por humanos. Ao total obtivemos 115 respostas, que resultaram em 488 sequências únicas e válidas. Além disso, o dono do canal MindingTheData nos enviou 85 sequências humanas que ele coletou em seu experimento, resultando então em 573 sequências. Para as sequências de máquina (pseudo-aleatórias), utilizamos um script em Python, gerando mais 573 exemplos, a fim de manter o balanceamento entre as classes. Ao total, o conjunto de dados possui 1140 sequências únicas.

A partir das sequências, foram extraídas diversas *features*, que servem como as entradas da rede neural. Algumas delas são: número de 0s, número de transições entre 0 e 1, complexidade de lempel-ziv. Ao total, foram criadas X features e foram selecionadas Y para serem utilizadas na rede neural após um processo de *feature selection*.

## Rede Neural

A rede neural foi criada utilizando a biblioteca PyTorch e possui a seguinte arquitetura:

- Totalmente conectada;
- Y neurônios na camada de entrada;
- 2 camadas ocultas com 32 neurônios cada, com função de ativação ReLU;
- Camada de saída com 1 neurônio, com função de ativação Sigmoid.

A rede neural foi treinada utilizando o algoritmo de otimização Adam e a função de perda Binary Cross Entropy Loss (BCE Loss). O treinamento foi realizado por 431 épocas, com um batch size de 16.

## Resultados


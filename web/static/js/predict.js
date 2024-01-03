async function predict() {
    const errado = document.getElementById('errado');
    const certo = document.getElementById('certo');

    errado.style.display = 'flex';
    certo.style.display = 'flex';

    const seq = document.querySelector('.example-sequence').value;
    const predictionElement = document.querySelector('.prediction');
    const errorMessage = document.querySelector('.error-message');

    if (seq.length != 50 || !seq.match(/^[01]+$/i)) {
        errorMessage.style.display = 'flex';
        if (predictionElement.style.display === 'flex') {
            predictionElement.style.display = 'none';
        }
        return;
    }

    try {
        const response = await fetch('/predict/' + seq);
        const data = await response.json();

        document.getElementById('prediction-value').textContent = data.predtxt;
        document.getElementById('prediction-value').val = data.pred;
        document.getElementById('confidence-value').textContent = data.conf + '%';

        errorMessage.style.display = 'none';
        predictionElement.style.display = 'flex';
    } catch (error) {
        console.error('Erro:', error);
        errorMessage.style.display = 'flex';
    }
}

document.getElementById('enviar').addEventListener('click', predict);

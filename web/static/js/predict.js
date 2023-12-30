async function predict() {
    const seq = document.querySelector('.example-sequence').value;

    // TODO: Melhorar o tratamento de erros mudando o CSS
    if (seq.length != 50) {
        alert('A sequência deve ter pelo menos 50 caractéres!');
        return;
    }

    if (!seq.match(/^[01]+$/i)) {
        alert('A sequência deve conter apenas os caracteres 0 ou 1');
        return;
    }

    await fetch('/predict/' + seq)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            document.getElementById('prediction-value').textContent = data.pred.toUpperCase();
            document.getElementById('confidence-value').textContent = data.conf + '%';
        })
        .catch(error => console.error('Erro:', error));

    document.querySelector('.prediction').style.display = 'flex';
}

document.getElementById('enviar').addEventListener('click', predict);
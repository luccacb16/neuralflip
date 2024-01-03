function enviarFeedback(feedbackTipo) {
    const seq = document.querySelector('.example-sequence').value;
    let label = Number(document.getElementById('prediction-value').val);

    if (feedbackTipo === 'errado') {
        label = 1 - label;
    }

    fetch('/feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            seq: seq,
            label: label
        })
    })
    .then(response => {
        if (response.ok) {
            const errado = document.getElementById('errado');
            const certo = document.getElementById('certo');

            errado.style.display = 'none';
            certo.style.display = 'none';

            fetch('/retrain')
            .then(response => response.json())
            .then(data => {
                console.log(data)
            })
            .catch(error => console.error('Erro na solicitação:', error));

        } else {
            console.error('Falha ao enviar feedback da predição');
        }
    })
    .catch(error => console.error('Erro na solicitação:', error));
}

document.getElementById('errado').addEventListener('click', () => enviarFeedback('errado'));
document.getElementById('certo').addEventListener('click', () => enviarFeedback('certo'));

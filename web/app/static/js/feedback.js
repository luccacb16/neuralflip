function feedback(feedback) {
    return function(feedback) {

        const seq = document.querySelector('.example-sequence').value;
        let label = Number(document.getElementById('prediction-value').val);

        if (feedback === 'errado') {
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
            } else {
                console.error('Falha ao enviar feedback da predição');
            }
        })
        .catch(error => console.error('Erro na solicitação:', error));

    }
}

const errado = feedback('errado');
const certo = feedback('certo');

document.getElementById('errado').addEventListener('click', errado);
document.getElementById('certo').addEventListener('click', certo);
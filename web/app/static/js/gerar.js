import { atualizarContador } from './contador.js';

function gerar() {
    fetch('/gerar')
        .then(response => response.json())
        .then(data => {
            const inputSequence = document.querySelector('.example-sequence');
            inputSequence.value = data.seq;
            inputSequence.style.opacity = 1;

            atualizarContador();
        })
        .catch(error => console.error('Erro:', error));
}

function alterarOpacidadeAoDigitar() {
    this.style.opacity = 1;
}

document.querySelector('.generate-button').addEventListener('click', gerar);
document.querySelector('.example-sequence').addEventListener('input', alterarOpacidadeAoDigitar);
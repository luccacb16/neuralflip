import { atualizarContador } from './contador.js';

function gerar() {
    fetch('/gerar')
        .then(response => response.json())
        .then(data => {
            document.querySelector('.example-sequence').value = data.seq;
            document.querySelector('.example-sequence').style.opacity = 1;

            atualizarContador();
        })
        .catch(error => console.error('Erro:', error));
}

document.querySelector('.generate-button').addEventListener('click', gerar);
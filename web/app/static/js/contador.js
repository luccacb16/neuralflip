export function atualizarContador() {
    const inputSequence = document.querySelector('.example-sequence');
    const counter = document.querySelector('.sequence-counter');

    let inputLength = inputSequence.value.length;

    if (inputLength > 50) {
        inputSequence.value = inputSequence.value.substring(0, 50);
        inputLength = 50;
    }

    counter.textContent = `${inputLength}/50`;
}

const inputSequence = document.querySelector('.example-sequence');
inputSequence.addEventListener('input', atualizarContador);

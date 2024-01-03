document.addEventListener('DOMContentLoaded', () => {
    const dropdowns = document.querySelectorAll('.dropdown');

    // Atualiza o idioma selecionado com base no valor armazenado
    const storedLanguage = localStorage.getItem('language');
    if (storedLanguage) {
        updateSelectedLanguage(storedLanguage);
    }

    dropdowns.forEach(dropdown => {
        const select = dropdown.querySelector('.select');
        const caret = dropdown.querySelector('.caret');
        const menu = dropdown.querySelector('.menu');
        const options = dropdown.querySelectorAll('.menu li');
        const selected = dropdown.querySelector('.selected');

        const openMenu = () => {
            caret.classList.add('caret-rotate');
            menu.classList.add('menu-open');
        };

        const closeMenu = () => {
            caret.classList.remove('caret-rotate');
            menu.classList.remove('menu-open');
        };

        select.addEventListener('mouseover', openMenu);
        menu.addEventListener('mouseover', openMenu);
        dropdown.addEventListener('mouseleave', closeMenu);

        options.forEach(option => {
            option.addEventListener('click', () => {
                const language = option.dataset.value;
                selected.dataset.value = language;
                selected.innerHTML = option.innerHTML;
                localStorage.setItem('language', language); // Armazena o idioma selecionado

                fetch('/language', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        language: language
                    })
                })
                .then(response => {
                    if (response.ok) {
                        window.location.reload(); // Recarrega a página
                    } else {
                        console.error('Falha ao mudar o idioma');
                    }
                })
                .catch(error => console.error('Erro na solicitação:', error));

                options.forEach(opt => {
                    opt.classList.remove('active');
                });
                option.classList.add('active');
                closeMenu();
            });
        });
    });
});

function updateSelectedLanguage(language) {
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
        const selected = dropdown.querySelector('.selected');
        const options = dropdown.querySelectorAll('.menu li');

        options.forEach(option => {
            if (option.dataset.value === language) {
                option.classList.add('active');
                selected.innerHTML = option.innerHTML;
                selected.dataset.value = language;
            } else {
                option.classList.remove('active');
            }
        });
    });
}

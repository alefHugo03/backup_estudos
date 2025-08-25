// static/script.js

// Este evento garante que o script só será executado quando todo o HTML for carregado.
document.addEventListener('DOMContentLoaded', function() {
    console.log('script.js carregado com sucesso!');

    // --- Lógica para o ano atual no rodapé ---
    const currentYearSpan = document.getElementById('currentYear');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }

    // --- Lógica para fechar mensagens flash automaticamente (opcional) ---
    // Você pode usar isso se quiser que as mensagens de alerta sumam após um tempo
    // const alerts = document.querySelectorAll('.alert');
    // alerts.forEach(alert => {
    //     new bootstrap.Alert(alert); // Inicializa o alerta do Bootstrap para o botão de fechar
    //     setTimeout(() => {
    //         const bsAlert = bootstrap.Alert.getInstance(alert);
    //         if (bsAlert) {
    //             bsAlert.close();
    //         } else {
    //             alert.remove(); // Remove diretamente se a instância não for encontrada
    //         }
    //     }, 5000); // Fecha após 5 segundos
    // });

    // --- Exemplo de função para mudar o tema (se você tiver botões/inputs para isso) ---
    // Esta função é chamada do HTML (ex: <button onclick="changeTheme('dark')">)
    // Ela faz uma requisição POST para a rota /settings para alterar o tema.
    // A rota /settings no app.py já lida com a mudança de tema.
    window.changeTheme = function(theme) {
        fetch('/settings', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'action=change_theme&theme_preference=' + theme
        }).then(response => {
            if (response.ok) {
                // Recarrega a página para que o Flask renderize o novo tema
                window.location.reload();
            } else {
                console.error('Erro ao mudar o tema. Status:', response.status);
                // Você pode querer mostrar uma mensagem de erro ao usuário aqui
            }
        }).catch(error => {
            console.error('Erro de rede ao tentar mudar o tema:', error);
            // Mensagem de erro de conexão
        });
    };
});
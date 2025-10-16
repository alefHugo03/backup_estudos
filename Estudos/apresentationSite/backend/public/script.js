// No seu arquivo: backend/public/script.js

// --- As variáveis que selecionam os elementos do HTML ---
const btnMenu = document.getElementById("btn-menu");
const inputEmail = document.getElementById("nome");
const inputSenha = document.getElementById("senha");
const avisoElemento = document.getElementById("aviso");

// --- Adiciona o evento de clique ao botão ---
btnMenu.addEventListener("click", processarDados);


// --- Função principal que usa o fetch ---
function processarDados() {

    // --- PARTE 1: PREPARAÇÃO (O que vamos pedir?) ---
    // Coletamos os dados do formulário que o usuário digitou.
    const dadosParaEnviar = {
        email: inputEmail.value,
        senha: inputSenha.value
    };

    console.log("Frontend: Preparando para enviar o pedido:", dadosParaEnviar);

    // ========================================================================
    // ▼▼▼ AQUI COMEÇA A CHAMADA FETCH ▼▼▼
    // ========================================================================

    fetch('/login', { // O 'pedido' começa. O destino é a rota '/login' do nosso servidor.

        // Detalhe 1: O MÉTODO (O que você quer fazer?)
        // 'POST' significa que estamos ENVIANDO dados para o servidor para que ele
        // processe ou salve algo. (Outra opção comum seria 'GET' para apenas buscar dados).
        method: 'POST',

        // Detalhe 2: OS CABEÇALHOS (Em que "idioma" estamos falando?)
        // Estamos avisando ao servidor: "Ei, os dados que estou enviando
        // no corpo do pedido estão no formato JSON."
        headers: {
            'Content-Type': 'application/json',
        },

        // Detalhe 3: O CORPO (Qual é o conteúdo do pedido?)
        // Aqui estão os dados que queremos enviar. O corpo da requisição precisa ser uma string.
        // JSON.stringify() converte nosso objeto JavaScript (dadosParaEnviar)
        // em uma string no formato JSON, que é como o texto viaja pela internet.
        body: JSON.stringify(dadosParaEnviar),

    }) // --- Fim da configuração do 'pedido' ---

    // ========================================================================
    // ▼▼▼ LIDANDO COM A RESPOSTA (O que fazer quando o garçom voltar?) ▼▼▼
    // ========================================================================

    // O fetch é uma "Promessa". Ele promete que uma resposta chegará no futuro.
    // O .then() é executado QUANDO a resposta do servidor finalmente chega.
    .then(response => {
        console.log("Frontend: O 'garçom' voltou com a resposta bruta do servidor.", response);
        // A 'response' que chega aqui é a resposta HTTP completa (status, cabeçalhos, etc.).
        // O conteúdo (body) ainda está em formato de texto.
        // response.json() é outra promessa que "lê" o corpo da resposta e o
        // converte de uma string JSON para um objeto JavaScript que podemos usar.
        return response.json();
    })

    // Este segundo .then() é executado QUANDO a promessa de response.json() é resolvida.
    .then(data => {
        console.log("Frontend: A resposta foi 'desempacotada' para um objeto JavaScript:", data);
        // 'data' é o objeto JavaScript final que o servidor enviou.
        // No nosso caso, é algo como: { mensagem: "Login bem-sucedido..." }
        // Agora podemos usar esses dados para atualizar nossa página!
        avisoElemento.innerHTML = data.mensagem;
    })

    // ========================================================================
    // ▼▼▼ LIDANDO COM ERROS (E se o pedido der errado?) ▼▼▼
    // ========================================================================

    // Se algo der errado na comunicação (servidor offline, erro de rede, etc.),
    // o código dentro do .catch() é executado, evitando que a aplicação quebre.
    .catch(error => {
        console.error("Frontend: Ocorreu um erro na comunicação com o servidor.", error);
        avisoElemento.innerHTML = "Falha na comunicação. Tente novamente.";
    });
}
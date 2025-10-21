/* Pagina de cadastro  */
const btmCriar = document.getElementById("btn-menu-criar");
const inputNome = document.getElementById("nome");
const inputEmail = document.getElementById("email");
const inputNascimento = document.getElementById("data");
const inputSenha = document.getElementById("senha");
const inputConfirmarSenha = document.getElementById("senhaDois");
const etapa = ["avisoNome", "avisoEmail", "avisoData", "avisoSenha", "avisoSenhaDois"];

btmCriar.addEventListener("click", processarDadosCadastro)

function processarDadosCadastro() {
    
    etapa.forEach(limparAviso);

    const nome = validarNome();
    const email = validarEmail();
    const nascimento = validarData();
    const senha = validarSenha();
    const confirmarSenha = validarConfirmarSenha(senha);

    if (!nome || !email || !nascimento || !senha || !confirmarSenha) return; 

    // 4. Envia para o servidor
    const dadosParaEnviar = {
        nome: nome, 
        email: email,
        nascimento: nascimento,
        senha: senha
    };

    console.log("Dados validados, enviando:", dadosParaEnviar);

    fetch('/cadastro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dadosParaEnviar),
    })
    .then(response => {
        if (response.ok) {
            alert("Cadastro realizado com sucesso!");
        } else {
            alert("Ocorreu um erro no cadastro. Tente novamente.");
        }
    })
    .catch(error => {
        console.error("Erro na requisição:", error);
        alert("Não foi possível conectar ao servidor.");
    });
};

const avisoFalas = (fala , etapa) => {
    const avisoElement = document.getElementById(etapa);

    avisoElement.innerHTML = fala;
    avisoElement.classList.add('aviso-ativo');
    setTimeout(() => { 
        avisoElement.classList.remove('aviso-ativo');
        avisoElement.innerHTML = ""; 
    }, 6000);
    return;
};

const limparAviso = (etapa) => {
    const avisoElement = document.getElementById(etapa);
    if (avisoElement) {
        avisoElement.innerHTML = ""; 
        avisoElement.classList.remove('aviso-ativo');
    }
};



const validarNome = () => {
    const nome = inputNome.value;
    const nomeRegex = /^[a-zA-Z\s]+$/;
    const nomeFalas = ["O campo nome não pode estar vazio.", "O nome deve conter mais de 3 letras.", "O nome deve conter apenas letras e espaços."];
    const ID_AVISO = etapa[0]; // "avisoNome"

    if (nome === "") return avisoFalas(nomeFalas[0], ID_AVISO); 
    if (nome.length < 3) return avisoFalas(nomeFalas[1] , ID_AVISO);
    if (!nomeRegex.test(nome)) return avisoFalas(nomeFalas[2], ID_AVISO);

    // Se passou, limpa qualquer aviso antigo e retorna o valor
    limparAviso(ID_AVISO); // CORRIGIDO
    return nome;
};

const validarEmail = () => {
    const email = inputEmail.value;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    // CORRIGIDO: Adicionado 'const'
    const nomeFalas = ["O campo email não pode estar vazio.", "Por favor, insira um email válido."];
    const ID_AVISO = etapa[1];

    if (email === "") return avisoFalas(nomeFalas[0], ID_AVISO); 
    if (!emailRegex.test(email)) return avisoFalas(nomeFalas[1], ID_AVISO);

    limparAviso(ID_AVISO); // ADICIONADO
    return email;
};

const validarData = () => {
    const dataString = inputNascimento.value; 
    const nomeFalas = ["Por favor, selecione sua data de nascimento.", "A data de nascimento não pode ser uma data no futuro.", "Você deve ter pelo menos 18 anos para se cadastrar."];
    const ID_AVISO = etapa[2];

    if (!dataString) return avisoFalas(nomeFalas[0], ID_AVISO);

    const hoje = new Date();
    hoje.setHours(0, 0, 0, 0);
    const parts = dataString.split('-');
    const dataSelecionada = new Date(parts[0], parts[1] - 1, parts[2]);

    if (dataSelecionada > hoje) return avisoFalas(nomeFalas[1], ID_AVISO);

    const dataMinima = new Date(hoje);
    dataMinima.setFullYear(hoje.getFullYear() - 18);
    if (dataSelecionada > dataMinima) return avisoFalas(nomeFalas[2], ID_AVISO);
    
    limparAviso(ID_AVISO);
    return dataString; 
};

const validarSenha = () => {
    const senha = inputSenha.value;
    const nomeFalas = ["O campo senha não pode estar vazio.", "A senha deve ter pelo menos 6 caracteres."];
    const ID_AVISO = etapa[3];

    if (senha === "") return avisoFalas(nomeFalas[0], ID_AVISO);
    if (senha.length < 6) return avisoFalas(nomeFalas[1], ID_AVISO);
    
    limparAviso(ID_AVISO);
    return senha;
};

const validarConfirmarSenha = (senha) => {
    const confirmarSenha = inputConfirmarSenha.value;
    const nomeFalas = ["O campo não pode estar vazio.", "As senhas não conferem!"];
    const ID_AVISO = etapa[4];

    if (confirmarSenha === "") return avisoFalas(nomeFalas[0], ID_AVISO);
    if (senha !== confirmarSenha) return avisoFalas(nomeFalas[1], ID_AVISO);

    limparAviso(ID_AVISO);
    return true;
};
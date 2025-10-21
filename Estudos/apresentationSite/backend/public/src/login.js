/*  Pagina principal  */
const btmEntrar = document.getElementById("btnEntrar");
const cadastroEmail = document.getElementById("emailEntrar");
const cadastroSenha = document.getElementById("senhaEntrar");
const etapa = ["avisoEmail", "avisoSenha"];

btmEntrar.addEventListener('click', processarDadosLogin);


function processarDadosLogin() {
    const senha = validarSenha();
    const email = validarEmail();
    
    if (!email && !senha) return;


    const dadosParaEnviar = {
        email: email,
        senha: senha
    };

    console.log("Dados de login:", dadosParaEnviar);

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(dadosParaEnviar),
    })
    .then(response => {
        if (response.ok) {
            alert("Login realizado com sucesso!");
        } else {
            alert("Credenciais inválidas. Tente novamente.");
        }
    })
    .catch(error => {
        console.error("Erro na requisição:", error);
        alert("Não foi possível conectar ao servidor.");
    });
}

const validarEmail = () => {
    const email = cadastroEmail.value;
    const avisoElement =  document.getElementById("avisoEmail");
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    nomeFalas = ["Digite um email válido", "O campo não pode estar vazio."]

    if (email === "") return avisoFalas(nomeFalas[1], etapa[0]);
    if (!emailRegex.test(email)) return avisoFalas(nomeFalas[0], etapa[0]);
        
    avisoElement.innerHTML = ""; 
    avisoElement.classList.remove('aviso-ativo');
    return email;
};


const validarSenha = () => {
    const senha = cadastroSenha.value; 
    const avisoElement = document.getElementById("avisoSenha");
    nomeFalas = ["Digite uma senha válida", "O campo não pode estar vazio."]

    if (senha === "") return avisoFalas(nomeFalas[1], etapa[1]);
    if (senha.length < 6) return avisoFalas(nomeFalas[0], etapa[1]);

    avisoElement.innerHTML = ""; 
    avisoElement.classList.remove('aviso-ativo');
    
    return senha;
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
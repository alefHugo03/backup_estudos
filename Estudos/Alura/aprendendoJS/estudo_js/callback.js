// setTimeout(function () {
//     console.log("Olá, mundo!");
// },2000);

const calcularDesconto = (total, desconto) => {
    return total * (1 - (desconto / 100));
}

// console.log(calcularDesconto(100,20));


function responderUsuario(nome, callback) {
    console.log(`Processando sua pergunta...\n`);
    setTimeout(() => {
        callback(nome)
    }, 3000)
}

function mostrarResposta(nome) {
    console.log(`Olá, ${nome}! Aqui está a resposta para sua dúvida.`)
}

// responderUsuario('Alef', mostrarResposta);


function gerarMensagem(nota, desempenho) {
    console.log(`Pontuação: ${nota}`);
    desempenho(nota)
}

function avaliarDesempenho(nota) {
    if (nota >= 7) { console.log("Parabéns! Você foi aprovado!"); };
    if (nota >= 5 && nota < 7) { console.log("Aprovado"); };
    if (nota < 5) { console.log("Reprovado!") };
}

gerarMensagem(5, avaliarDesempenho);

/*
    Melhorando o CallBack
*/

const calcularMedia = (nota1, nota2, nota3, resposta, desempenho) => { const nota = (nota1 + nota2 + nota3) / 3; return resposta(nota, desempenho); };

// calcularMedia(9, 6, 7, gerarMensagem, avaliarDesempenho)


/* 
    Melhorando mais um pouco
*/

const nota = [9, 9, 10];

const calculoMedia = (array, resposta, desempenho) => {
    let soma = 0;
    for (let i = 0; i < array.length; i++) {
        soma += array[i];
    }
    media = soma / array.length;
    return resposta(media, desempenho);
};

calculoMedia(nota, gerarMensagem, avaliarDesempenho)

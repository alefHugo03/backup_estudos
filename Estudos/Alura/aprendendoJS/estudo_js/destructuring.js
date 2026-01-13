const Carla = {
    nome : 'Carla Maria',
    profissao : 'Estudante',
    idade : '18'
}

// const {nome, idade} = Carla;

// console.log(nome);
// console.log(idade);

function saudacao({ nome, idade }) {
    console.log('Prazer em te conhecer', nome)
    if (idade >= 18){
        console.log('Você é maior de idade')
    }
}
saudacao(Carla);
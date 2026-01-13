const user = {
    nome: 'Alef',
    nascimento: '2000-03-27',
    cpf:'12332112332',
    pontuacao: 4000,
    trofeus: ['speedruner', 'indie']
};

user.calculaIdade = function() {
    const anoNasc = parseInt(this.nascimento.slice(0, 4));
    const anoAtual = new Date().getFullYear();

    const idade = anoAtual - anoNasc;
    console.log(`Tem ${idade} anos`);
}

user.calculaIdade();
function tratarErros(erro) {
    if (erro.code === 'ENOENT') {
        throw new Error('Caminho de arquivo incorreta para o arquivo selecionados')
    }
    else 'erro na publicação'
}

module.exports = tratarErros;
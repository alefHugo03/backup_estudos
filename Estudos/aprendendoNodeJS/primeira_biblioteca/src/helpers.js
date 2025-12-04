function filtraOcorrencias(paragrafo) {
    return Object.keys(paragrafo).filter(chave => paragrafo[chave] > 1)
}

function montaSaidaArquivo (listaPalavras) {
    let textoFinal = '';
    listaPalavras.forEach((paragrafo, indice) => {
        const duplicadas = filtraOcorrencias(paragrafo).join(', ');
         if (duplicadas == '') {
            return textoFinal += `Paragrafo ${indice + 1} sem duplicadas\n`
        }

        textoFinal += `Palavras duplicadas no parágrafo ${indice + 1}: ${duplicadas} \n`
    });

    return textoFinal;
}

export { montaSaidaArquivo }
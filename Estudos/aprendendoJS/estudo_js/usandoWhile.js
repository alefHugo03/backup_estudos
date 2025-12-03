contador = 0;

console.log('******************\n\n Contagem até 10 \n\n******************')

while (contador <= 10) {
    if (contador < 10) {
        console.log(contador);
    }
    else {
        console.log('Acabou');
    }
    contador++;
}

console.log('******************\n\n Contagem regressiva \n\n******************')


lancamento = 10;

while (lancamento >= 0) {
    if (lancamento > 0) {
        console.log(lancamento);
    }
    else {
        console.log('Lançar!');
    }
    lancamento--;
}
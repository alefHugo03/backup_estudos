const estudanteReprovou = function (notaFinal, faltas) {
    if (notaFinal < 7 || faltas > 4) {
        return true;
    } else {
        return false;
    }
}

console.log(estudanteReprovou(6, 5));
console.log(estudanteReprovou(8, 3));
/*
 hoisting = içar
 funções declaradas com function são içadas
 funções declaradas com const não são içadas
 funciona com uma ordem
*/

//arrow function
const estudanteReprovou2 = (notaFinal, faltas) => {
    if (notaFinal < 7 || faltas > 4) {
        return true;
    } else {
        return false;
    }
}

const exibeNome = nome => nome;
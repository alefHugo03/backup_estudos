const notas = [10, 6.5, 8, 7.5, 9, 5, 3, 4, 2, 1];

mediaNotas =0;

for (let i = 0; i < notas.length; i++) {
    mediaNotas += notas[i];
}

const mediaFinal = mediaNotas / notas.length;

console.log(`A média da turma é ${mediaFinal}`);

// usando of

for (let nota of notas) {
    mediaNotas += nota;
}

const mediaFinal2 = mediaNotas / notas.length;

console.log(`A média da turma é ${mediaFinal2}`);

// usando forEach

const notas3 = [10, 6.5, 8, 7.5, 9, 5, 3, 4, 2, 1];
let mediaNotas3 = 0;

notas3.forEach(nota => {
    mediaNotas3 += nota;
});

const mediaFinal3 = mediaNotas3 / notas3.length;

console.log(`A média da turma é ${mediaFinal3}`);
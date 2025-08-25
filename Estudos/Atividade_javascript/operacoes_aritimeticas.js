const notaPrimeiroBi = 8;
const notaSegundoBi = 7;
const notaTerceiroBi = 5.25;
const notaQuartoBi = 8.5;

let total = (notaPrimeiroBi + notaSegundoBi + notaTerceiroBi + notaQuartoBi) / 4;

if (total < 7) {
    console.log("Aluno reprovado");
    console.log(`A méia do aluno é ${total.toFixed(2)}`);
}
else {
    console.log("Aluno aprovado");
    console.log(`A méia do aluno é ${total.toFixed(2)}`);
}

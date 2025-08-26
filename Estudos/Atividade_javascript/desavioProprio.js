//  Criar um avaliador de aprovação para os estudantes de uma escola.

const nomeEstudante = "João";
const nota1Bim = 9;
const nota2Bim = 7;
const nota3Bim = 8;
const nota4Bim = 6;
const faltas = 2;

const aprovação = (nota1, nota2, nota3, nota4, faltas) => {
    const media = (nota1Bim + nota2Bim + nota3Bim +nota4Bim) / 4;
    if (faltas < 4 && media >= 7) {
        return "Aprovado";
    } 
    if (faltas >= 4 && media >= 7) {
        return `aluno ${nomeEstudante} foi reprovado por ter ${faltas} faltas e média ${media}`;
    }
    if (media < 7) {
        return `aluno ${nomeEstudante} foi reprovado por ter média ${media}`;
    }
    if (faltas >= 4) {
        return `aluno ${nomeEstudante} foi reprovado por ter média ${faltas}`;
    }
}
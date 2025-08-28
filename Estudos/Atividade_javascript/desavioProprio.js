//  Criar um avaliador de aprovação para os estudantes de uma escola.

const nomeEstudante = "João";
const notas = [9, 7, 8, 6];

const faltas = 2;

const aprovação = (notas, faltas) => {
    const media = (notas[0] + notas[1] + nota[2] +nota[3]) / notaa.length;
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
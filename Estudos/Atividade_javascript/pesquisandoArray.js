const alunos = ["João", "Juliana", "Ana", "Caio"];
const notas = [0, 8, 7.5, 9];

// cria uma array que armazna duas dimensões
const alunosNotas = [alunos, notas];

function pesquisandoAluno(alunos) {
    // Verificar se o aluno está na lista
    if (alunosNotas[0].includes(alunos)) {
        // Desestruturar a array de duas dimensões
        const [alunos, notas] = alunosNotas;
        // Achar o índice do aluno
        const indice = alunos.indexOf(alunos);
        const mediaAluno = notas[indice]
        return `${aluno} está na lista, e sua média é ${mediaAluno}`;
    }
    else{
        return "Aluno não está cadastrado";
    }
}


const fs = require('fs');
const bancoCsv = 'database.csv'
const banco = fs.readFileSync(bancoCsv, 'utf8');

const regexTelefone = /\(\d+\)\s\d+-\d+/g

const matchTelefone = banco.match(regexTelefone);
console.log(matchTelefone);

const patterCel = /\(\d{2}\)\s\d{4,5}-\d{4}/g
const matchCelular = banco.match(patterCel);
console.log(matchCelular);

/* metachards
g= geral
\ =barra de escapamento
\d = dígito
\s = espaço em branco
+ = um ou mais dígitos
() = captura de grupo
- = hífen
\b = limite de palavra
\w = palavra
\b\w+ = palavra completa

POSIX
[[:digit:]]	Qualquer dígito.
[[:alpha:]]	Qualquer caractere alfabético.
[[:alnum:]]	Qualquer caractere alfanumérico.
[[:blank:]]	Espaço em branco ou caractere de tabulação.
[[:space:]]	Qualquer caractere de espaço em branco.
[[:lower:]]	Qualquer letra minúscula.
[[:upper:]]	Qualquer letra maiúscula.
[[:print:]]	Qualquer caractere imprimível, incluindo espaços.
[[:punct:]]	Qualquer caractere de pontuação.
[[:graph:]]	Qualquer caractere imprimível, excluindo espaços.
[[:xdigit:]]	Qualquer dígito hexadecimal (0-9, a-f, A-F).
[[:cntrl:]]	Qualquer caractere de controle.

Meta caracteres Ragex
.	Qualquer caractere, exceto quebras de linha.
*	Zero ou mais ocorrências do caractere ou grupo anterior.
+	Uma ou mais ocorrências do caractere ou grupo anterior.
?	Zero ou uma ocorrência do caractere ou grupo anterior.
|	Alternância, corresponde a um dos padrões à esquerda ou à direita.
()	Grupo de captura, agrupa caracteres para aplicar metacaracteres a eles.
[]	Classe de caracteres, corresponde a qualquer caractere dentro dos colchetes.
[^]	Classe de caracteres negada, corresponde a qualquer caractere que não esteja dentro dos colchetes.
^	ncora de início de linha, corresponde ao início de uma linha.
$	ncora de final de linha, corresponde ao final de uma linha.
\	Escape, permite escapar metacaracteres para correspondê-los literalmente.
{}	Quantificador personalizado, especifica o número exato ou faixa de repetições.

*/
const fs = require('fs');
const bancoCsv = 'database.csv'
const banco = fs.readFileSync(bancoCsv, 'utf8');

/* const regexCpf = /\(\d+\)\s\d+-\d+/g */
const regexCpf = /\d{3}[.-]?\d{3}[.-]?\d{3}[.-]?\d{2}/g

const matchCpf = banco.match(regexCpf);
console.log(matchCpf);

/*
REGRAS
[a-z]	Qualquer letra minúscula de 'a' a 'z'	"a", "m", "z"
[0-9]	Qualquer dígito de 0 a 9	"0", "7", "9"
[A-Za-z]	Qualquer letra maiúscula ou minúscula	"A", "b", "Z"
[0-9A-Fa-f]	Qualquer caractere hexadecimal	"1", "A", "d"
[^0-9]	Qualquer caractere que não seja um dígito	"a", "B", "!"
[aeiou]	Qualquer vogal minúscula	"a", "e", "o"
[^aeiou]	Qualquer caractere que não seja uma vogal	"b", "z", "1"
[|?/’]	Caracteres literais	"|", "/", " ? ", “‘”

\d	Qualquer dígito decimal	"0", "7", "9"
\D	Qualquer caractere que não seja um dígito	"a", "B", "!"
\w	Qualquer caractere alfanumérico	"A", "b", "0"
\W	Qualquer caractere que não seja alfanumérico	"!", "@", " "
\s	Qualquer caractere de espaço em branco	" ", "\t", "\n"
\S	Qualquer caractere que não seja espaço em branco	"a", "B", "9"

\[	Colchete de abertura [ literal	"["
\]	Colchete de fechamento ] literal	"]"
\.	Ponto . literal	"."
\+	Sinal de adição + literal	"+"
\\	Escape \ literal	""
*/
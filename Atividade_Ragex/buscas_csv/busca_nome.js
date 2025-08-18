const fs = require('fs');
const bancoCsv = 'database.csv';
const banco = fs.readFileSync(bancoCsv, 'utf8');

const regexData = /^([A-Za-zÁ-ÿ]+)(?:\s([A-Za-zÁ-ÿ]+))+/gm

const matchData = banco.match(regexData);
console.log(matchData);

/* 
Quantificador	                Descrição	                                                                        Exemplo
*	                Coincide com 0 ou mais ocorrências do elemento anterior.	                        a* corresponde a "", "a", "aa", "aaa", etc.
+	                Coincide com 1 ou mais ocorrências do elemento anterior.	                        a+ corresponde a "a", "aa", "aaa", etc., mas não a "".
?	                Coincide com 0 ou 1 ocorrência do elemento anterior.	                            a? corresponde a "" ou "a".
{n}	                Coincide exatamente com “n” ocorrências do elemento anterior.	                    a{3} corresponde a "aaa", mas não a "aa" ou "a".
{n,}	            Coincide com pelo menos “n” ocorrências do elemento anterior.	                    a{2,} corresponde a "aa", "aaa", "aaaa", etc.
{n,m}	            Coincide com pelo menos “n” e no máximo “m” ocorrências do elemento anterior.	    a{2,4} corresponde a "aa",  "aaa" ou "aaaa", mas não a "a" ou "aaaaa"

*/
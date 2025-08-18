const fs = require('fs');
const bancoCsv = 'database.csv'
const banco = fs.readFileSync(bancoCsv, 'utf8');

/* const regexCpf = /\(\d+\)\s\d+-\d+/g */
const regexData = /\d{2}[./ ]?\d{2}[./ ]?\d{4}$/gm

const matchData = banco.match(regexData);
console.log(matchData);
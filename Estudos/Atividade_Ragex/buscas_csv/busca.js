const fs = require('fs');
const bancoCsv = 'database.csv'
const banco = fs.readFileSync(bancoCsv, 'utf8');

const regex = /Anna/

const matchRegex =banco.match(regex);

console.log(matchRegex)

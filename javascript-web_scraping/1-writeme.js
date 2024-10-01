#!/usr/bin/node
const fs = require('fs');
const arg = process.argv[2];
let data = process.argv[3];
fs.writeFile(arg, data,  'utf-8', (err) => {
if (err) {
console.log(err);
}
});

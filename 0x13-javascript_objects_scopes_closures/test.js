#!/usr/bin/node
const fs = require('fs');

function reader(filename) {
  try {
    contents = fs.readFileSync(filename, 'utf8');
    return contents;
  } catch (err) {
    console.log(err);
    return;
  }
}

function writeInfo (filename, content) {
  try {
    fs.writeFileSync(filename, content);
  } catch (err) {
    console.log(err);
  }
}

const a = reader('fileA');
const b = reader('fileB');
const c = a + b
writeInfo(c, 'fileC')
const final = reader('fileC');


console.log(a);
console.log(b);
console.log(final);

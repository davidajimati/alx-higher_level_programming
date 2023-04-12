#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

const fileA = args[0];
const fileB = args[1];
const fileC = args[2];

const a = reader(fileA);
const b = reader(fileB);
const c = a + b;
writeInfo(fileC, c);

function reader (filename) {
  try {
    contents = fs.readFileSync(filename, 'utf8');
    return contents;
  } catch (err) {
    console.log(err);
  }
}

function writeInfo (filename, content) {
  try {
    fs.writeFileSync(filename, content);
  } catch (err) {
    console.log(err);
  }
}

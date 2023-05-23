#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
fs.readFile(`${path}`, 'utf-8', (err, output) => {
  if (err) throw err;
  else {
    console.log(output);
  }
});

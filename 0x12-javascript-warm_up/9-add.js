#!/usr/bin/node
const args = process.argv;

const a = Number(args[2]);
const b = Number(args[3]);

function add (a, b) {
  console.log(a + b);
}

add(a, b);

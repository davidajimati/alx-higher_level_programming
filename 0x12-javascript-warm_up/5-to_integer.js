#!/usr/bin/node
const args = process.argv;
if (Number.isInteger(Number(args[2]))) {
  console.log(`My number: ${Number(args[2])}`);
} else {
  console.log('Not a number');
}

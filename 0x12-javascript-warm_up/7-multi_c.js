#!/usr/bin/node
const args = process.argv;
if (args.length < 2) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < Number(args[2]); i++) {
  console.log('C is fun');
}

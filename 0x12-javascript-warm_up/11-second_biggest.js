#!/usr/bin/node
let args = process.argv.slice(2);

if (args.length < 4) {
  console.log(0);
} else {
  args = args.map((i) => Number(i));
  args = args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}

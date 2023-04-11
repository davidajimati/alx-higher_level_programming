#!/usr/bin/node
const args = process.argv;

if (Number(args[2])) {
  const lim = Number(args[2]);

  for (let i = 0; i < lim; i++) {
    console.log('X'.repeat(lim));
  }
} else {
  console.log('Missing size');
}

#!/usr/bin/node
const list = require('./100-data.js').list;
let newArr = []
if (list.length == 0)
  console.log(newArr);

newArr = list.map((i) => i * list.indexOf(i));
console.log(list);
console.log(newArr);

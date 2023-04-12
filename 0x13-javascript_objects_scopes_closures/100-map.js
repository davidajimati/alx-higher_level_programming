#!/usr/bin/node
const list = require('./100-data.js').list;
let newArr = [];
if (list.length === 0) { console.log(newArr); } else {
  newArr = list.map((i, x) => i * x);
}
console.log(list);
console.log(newArr);

#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const newArr = list.map((value, index) => value * index);
console.log(newArr);

#!/usr/bin/node
const dict = require('./101-data.js').dict;

let newDict = {};
for (let key in dict) {
  if (!(dict[key] in newDict)) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
}
console.log(newDict);

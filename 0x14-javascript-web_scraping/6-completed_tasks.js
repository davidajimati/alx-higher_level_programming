#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const record = {};
    todos.forEach((todo) => {
      if (todo.record && record[todo.userId] === undefined) {
        record[todo.userId] = 1;
      } else if (todo.record) {
        record[todo.userId] += 1;
      }
    });
    console.log(record);
  }
});
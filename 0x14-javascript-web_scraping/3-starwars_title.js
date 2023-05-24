#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const target = process.argv[2];

request(url + target, (error, response, body) => {
  if (error) throw error;
  else {
    const ans = pushJSON.parse(body);
    console.log(ans.title);
  }
});

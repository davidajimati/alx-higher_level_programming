#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request.get(url, (err, resp) => {
  if (err) throw err;
  else {
    console.log('code:', resp.statusCode);
  }
});

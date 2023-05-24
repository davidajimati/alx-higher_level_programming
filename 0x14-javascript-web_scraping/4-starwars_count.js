#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, resp, body) {
  if (error) {
    console.log(error);
  } else if (resp.statusCode === 200) {
    const films = JSON.parse(body).results;
    let idx = 0;
    for (const movie in films) {
      const movieChars = films[movie].characters;
      for (const charIndex in movieChars) {
        if (movieChars[charIndex].includes('18')) {
          idx++;
        }
      }
    }
    console.log(idx);
  } else {
    console.log('An error occurred. Status code: ' + resp.statusCode);
  }
});

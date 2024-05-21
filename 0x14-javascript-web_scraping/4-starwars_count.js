#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes('/18/')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});

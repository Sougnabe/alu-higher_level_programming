#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2]; 

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach(film => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  }
});

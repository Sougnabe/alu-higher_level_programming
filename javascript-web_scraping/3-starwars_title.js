#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});

#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.
// The first argument is the movie ID.

const request = require('request');

const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);

  console.log(movie.title);
});

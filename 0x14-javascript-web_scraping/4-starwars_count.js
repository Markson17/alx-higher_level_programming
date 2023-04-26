#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;


  const wedgeAntillesMovies = films.filter((film) => {
    return film.characters.some((character) => {
      return character.endsWith('/18/');
    });
  });

  console.log(`Number of movies where Wedge Antilles is present: ${wedgeAntillesMovies.length}`);
});

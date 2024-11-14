#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const film = JSON.parse(body);
  const characterUrls = film.characters;

  characterUrls.forEach(function (characterUrl) {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.log(error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});

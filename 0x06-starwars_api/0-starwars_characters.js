#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error(`Error: Unable to fetch movie data (status code: ${res.statusCode})`);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  const fetchCharacter = (url, callback) => {
    request(url, (err, res, body) => {
      if (err) {
        callback(err, null);
        return;
      }

      if (res.statusCode !== 200) {
        callback(new Error(`Failed to fetch character (status code: ${res.statusCode})`), null);
        return;
      }

      const characterData = JSON.parse(body);
      callback(null, characterData.name);
    });
  };

  const characterNames = [];
  let completedRequests = 0;

  characters.forEach((url, index) => {
    fetchCharacter(url, (err, name) => {
      if (err) {
        console.error(err);
        return;
      }

      characterNames[index] = name;
      completedRequests++;

      if (completedRequests === characters.length) {
        characterNames.forEach((name) => console.log(name));
      }
    });
  });
});


#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie data
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
  const characterUrls = movieData.characters;

  // Fetch all characters in order
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) reject(err);
        else if (res.statusCode !== 200) reject(new Error(`Failed to fetch character: ${res.statusCode}`));
        else resolve(JSON.parse(body).name);
      });
    });
  };

  Promise.all(characterUrls.map(fetchCharacter))
    .then((characterNames) => {
      characterNames.forEach((name) => console.log(name));
    })
    .catch((err) => {
      console.error(err);
    });
});

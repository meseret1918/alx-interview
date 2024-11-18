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

  try {
    const film = JSON.parse(body);

    if (!film.characters) {
      console.error('Characters not found');
      return;
    }

    // Fetch all character names in the order they appear in the API response
    const characterPromises = film.characters.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
          if (err) return reject(err);
          try {
            const character = JSON.parse(body);
            resolve(character.name);
          } catch (e) {
            reject(e);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((names) => {
        console.log(names.join('\n'));
      })
      .catch((err) => {
        console.error(err);
      });
  } catch (e) {
    console.error('Failed to parse API response:', e.message);
  }
});


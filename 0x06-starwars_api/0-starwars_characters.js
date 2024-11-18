#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get movie ID from command-line args
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const film = JSON.parse(body);
    const characters = film.characters;

    // Use Promise.all to fetch all character details concurrently
    Promise.all(
      characters.map((charUrl) =>
        new Promise((resolve, reject) => {
          request(charUrl, (err, res, charBody) => {
            if (err) reject(err);
            resolve(JSON.parse(charBody).name);
          });
        })
      )
    )
      .then((names) => {
        console.log(names.join('\n'));
      })
      .catch((err) => console.error('Error fetching characters:', err));
  } catch (parseError) {
    console.error('Error parsing response:', parseError);
  }
});


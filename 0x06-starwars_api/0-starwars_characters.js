#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  fetchCharactersInOrder(characters, 0);
});

function fetchCharactersInOrder(characters, index) {
  if (index === characters.length) return;

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    
    console.log(JSON.parse(body).name);
    fetchCharactersInOrder(characters, index + 1);
  });
}

#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Construct the API URL to fetch movie details
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);
  
  // Extract the characters array
  const characters = movieData.characters;

  // Iterate through the characters list and fetch character details
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Parse the character's details and log the name
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});

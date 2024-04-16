#!/usr/bin/node
// This script fetches and prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Invalid status code:', charResponse.statusCode);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});


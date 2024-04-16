#!/usr/bin/node

const request = require('request');

async function makeRequestSync (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, _, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function main (id) {
  try {
    const response = await makeRequestSync(`https://swapi-api.alx-tools.com/api/films/${id}/`);
    for (const character of response.characters) {
      const response = await makeRequestSync(character);
      console.log(response.name);
    }
  } catch (error) {
    console.log(error);
  }
}

const id = process.argv[2];
main(id);

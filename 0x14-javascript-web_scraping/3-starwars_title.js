#!/usr/bin/node
/*script that prints the title of a Star Wars movie */

const request = require('request');
const URI = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(URI, function (error, response, body) {
  if (error) console.error(error);
  console.log(JSON.parse(body).title);
});

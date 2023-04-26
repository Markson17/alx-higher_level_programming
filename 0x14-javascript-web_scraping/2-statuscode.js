#!/usr/bin/node
// Script that display the status code of a GET request.
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log(`status code: ${response.statusCode}`);
});

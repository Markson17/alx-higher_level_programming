#!/usr/bin/node
// Script that reads and prints the content of a file.

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});

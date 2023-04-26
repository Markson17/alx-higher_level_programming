#!/usr/bin/node
// Script that computes the number of tasks completed by user id
const myArgs = process.argv.slice(2);

const request = require('request');
const link = myArgs[0];

request.get(link, { json: true }, (err, res, body) => {
  if (err) throw err;
  const fs = {};
  for (const resu of body) {
    if (resu.completed) {
      if (fs[resu.userId]) {
        fs[resu.userId]++;
      } else {
        fs[resu.userId] = 1;
      }
    }
  }
  console.log(fs);
});

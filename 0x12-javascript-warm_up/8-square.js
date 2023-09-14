#!/usr/bin/node
const { argv } = require('process');

const len = +argv[2];

if (argv.length === 2 || isNaN(len)) {
  console.log('Missing size');
} else if (argv.length === 3 && !isNaN(len)) {
  let x = '';

  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      x += 'X';
    }
    console.log(x);
    x = '';
  }
}

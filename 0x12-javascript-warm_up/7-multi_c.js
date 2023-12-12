#!/usr/bin/node
const { argv } = require('process');

if (argv.length === 2) {
  console.log('Missing number of occurrences');
} else if (argv.length === 3) {
  const len = +argv[2];
  if (!isNaN(len)) {
    for (let i = 0; i < len; i++) {
      console.log('C is fun');
    }
  }
}

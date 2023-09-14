#!/usr/bin/node
const { argv } = require('process');

let highest;
let highest2;

if (argv.length <= 3) {
  highest2 = 0;
} else if (argv.length === 4) {
  highest = +argv[2];
  highest2 = +argv[3];
  if (highest2 > highest) {
    highest2 = highest;
  }
} else {
  highest = +argv[2];
  highest2 = +argv[3];
  for (let i = 3; i < argv.length; i++) {
    if (+argv[i] > highest) {
      highest2 = highest;
      highest = +argv[i];
    }
  }
}

console.log(highest2);

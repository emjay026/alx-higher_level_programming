#!/usr/bin/node
const { argv } = require('process');

let a_ = +argv[2];

if (isNaN(a_)) {
  a_ = 1;
}

function factorial (a) {
  if (a === 1) {
    return 1;
  }
  return (a * factorial(a - 1));
}

console.log(factorial(a_));

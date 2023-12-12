#!/usr/bin/node
const { argv } = require('process');

const a_ = +argv[2];
const b_ = +argv[3];

function add (a, b) {
  console.log(a + b);
}

add(a_, b_);

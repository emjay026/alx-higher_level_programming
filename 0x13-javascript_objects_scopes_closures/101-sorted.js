#!/usr/bin/node

const dict = require('./101-data').dict;

// turn dict into a list of lists,
// where inner list represents key value pairs
const entries = Object.entries(dict);

// sort function of array object where a comparator
// is passed as argument
entries.sort((a, b) => a[1] - b[1]);

// reduce function of array object where a callback and
// initial value are passed.
const groupedDict = entries.reduce((acc, [key, value]) => {
  if (!acc[value]) {
    acc[value] = [];
  }
  acc[value].push(key);
  return acc;
}, {});

console.log(groupedDict);

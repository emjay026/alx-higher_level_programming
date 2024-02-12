#!/usr/bin/node

const callMeMoby = function (numTimes, callback) {
  for (let i = 0; i < numTimes; i++) {
    callback();
  }
};

module.exports = { callMeMoby };

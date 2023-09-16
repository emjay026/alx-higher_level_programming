#!/usr/bin/node

const callMeMoby = function (numTimes, callback) {
  if (numTimes <= 0) {
    return;
  }
  for (let i = 0; i < numTimes; i++) {
    callback();
  }
};

module.exports = { callMeMoby };

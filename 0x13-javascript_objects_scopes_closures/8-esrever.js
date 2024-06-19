#!/usr/bin/node
exports.esrever = function (list) {
  const len = Math.floor(list.length / 2) - 1;
  let j = list.length - 1;
  let temp = 0;
  for (let i = 0; i <= len; i++) {
    temp = list[i];
    list[i] = list[j];
    list[j] = temp;
    j--;
  }
  return list;
};

#!/usr/bin/node

const addMeMaybe = function (num, func) {
    func(num + 1);
};

module.exports = { addMeMaybe };

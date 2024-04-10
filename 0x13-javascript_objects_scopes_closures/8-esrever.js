#!/usr/bin/node
// function that returns the reversed version of a list:
// You are not allow to use the built-in method reverse
exports.esrever = function (list) {
  const NewArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    NewArray.push(list[i]);
  }
  return (NewArray);
};

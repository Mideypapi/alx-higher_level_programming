#!/usr/bin/node
// script that computes and prints a factorial
let MyNumber = process.argv[2];
MyNumber = parseInt(MyNumber, 10);
if (isNaN(MyNumber)) {
  console.log(1);
} else {
  console.log(factorial(MyNumber));
}

function factorial (number) {
  if (number === 0) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

#!/usr/bin/node
// script that prints the addition of 2 integers
let Number1 = process.argv[2];
let Number2 = process.argv[3];
Number1 = parseInt(Number1, 10);
Number2 = parseInt(Number2, 10);
if (isNaN(Number1)) {
  console.log(NaN);
} else if (isNaN(Number2)) {
  console.log(NaN);
} else {
  console.log(Number1 + Number2);
}

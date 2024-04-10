#!/usr/bin/node
// script that prints x times “C is fun”
let MyNumber = process.argv[2];
MyNumber = parseInt(MyNumber, 10);
if (isNaN(MyNumber)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < MyNumber; i++) {
    console.log('C is fun');
  }
}

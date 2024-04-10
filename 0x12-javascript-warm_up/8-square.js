#!/usr/bin/node
// script that prints a square
let MyNumber = process.argv[2];
MyNumber = parseInt(MyNumber, 10);
if (isNaN(MyNumber)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < MyNumber; i++) {
    console.log('X'.repeat(MyNumber));
  }
}

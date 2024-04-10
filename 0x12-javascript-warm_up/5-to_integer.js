#!/usr/bin/node
// script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer
let MyNumber = process.argv[2];
MyNumber = parseInt(MyNumber, 10);
if (isNaN(MyNumber)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + MyNumber);
}

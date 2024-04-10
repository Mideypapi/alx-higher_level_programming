#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const MyArray = [];
  for (let i = 2; i < process.argv.length; i++) {
    MyArray.push(parseInt(process.argv[i]));
  }
  MyArray.sort(mayor);
  MyArray.pop();
  console.log(MyArray[MyArray.length - 1]);
}

function mayor (elem1, elem2) {
  return elem1 - elem2;
}

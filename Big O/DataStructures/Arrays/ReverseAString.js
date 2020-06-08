//create a function that reverses a string
//sk creates algorithms

let exampleString = "SK creates algorithms";

//approach 1
function reverse(str) {
  //check input
  if (!str || str.length < 2 || typeof str != "string") {
    if (str.length < 2) {
      return str;
    } else {
      ("invalid input");
    }
  }

  let newArray = [];
  for (let i = str.length - 1; i >= 0, i--; ) {
    newArray.push(str[i]);
  }
  return newArray.join("");
}
console.log(reverse(exampleString));

//approach 2
function reverse_two(str) {
  if (!str || str.length < 2 || typeof str != "string") {
    if (str.length < 2) {
      return str;
    } else {
      ("invalid input");
    }
  }

  return str.split("").reverse().join("");
}

console.log(reverse_two(exampleString));

//aproach 3
const reverse_three = (str) => [...str].reverse().join("");

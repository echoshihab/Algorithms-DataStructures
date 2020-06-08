//given 2 arrays, creata  function that
//let's a user know (true/balse) whether these two arrays contain
//any commmon items

//for example: O (a*b)
const array1 = ["a", "b", "c", "x"];
const array2 = ["z", "y", "i"];

const array3 = ["a", "b", "c", "x"];
const array4 = ["z", "y", "x"];

function compare_arrays(array1, array2) {
  for (i = 0; i < array1.length; i++) {
    if (array2.includes(array1[i])) {
      return true;
    }
  }
  return false;
}

let result1 = compare_arrays(array1, array2);
let result2 = compare_arrays(array3, array4);

console.log(result1);
console.log(result2);

//better solution: time complexity = n + n = or O(n)

function compare_arrays2(arr1, arr2) {
  //loop through first array and create object where properties === items in the array
  let map = {};
  for (let i = 0; i < arr1.length; i++) {
    if (!map[arr1[i]]) {
      const item = arr1[i];
      map[item] = true;
    }
  }

  //loop through second array and check if item in second array exists on created object
  for (let k = 0; k < arr2.length; k++) {
    if (map[arr2[k]]) {
      return true;
    }
  }
  return false;
}

//alternate js solution

function compare_arrays3(arr1, arr2) {
  return arr1.some((value) => arr2.includes(value));
}

console.log(compare_arrays3(array3, array4));
console.log(compare_arrays3(array1, array2));

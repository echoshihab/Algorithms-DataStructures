//which one gets repeated first
//Given an array = [2,4,1,2,3,5,1,2,4]:
//it should return 2

//given an arra = [2,1,1,2,3,5,1,2,4]:
//it should return 1

//given an array = [2,3,4,5]:
//it should retrn undefined

//faster solution
function checkArray(array) {
  if (!Array.isArray(array)) {
    return undefined;
  }

  let hashTable = {};
  for (i = 0; i < array.length; i++) {
    if (!hashTable[array[i]]) {
      hashTable[array[i]] = array[i];
    } else {
      return hashTable[array[i]];
    }
  }
  return undefined;
}

console.log(checkArray([2, 3, 4, 5]));

//slower solutions -due to O(n^2),also outer loop will give a different
//number for example in [2,5,5,1,2,3]
function firstRecurringCharacter(input) {
  for (let i = 0; i < input.length; i++) {
    for (let j = i + 1; j < input.length; j++) {
      if (input[i] === input[j]) {
        return input[i];
      }
    }
  }
  return undefined;
}

console.log(firstRecurringCharacter([2, 4, 1, 2, 3, 5, 1, 2, 4]));

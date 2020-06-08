//merge 2 sorted array
//aproach 1
let firstArray = [0, 3, 4, 31];
let secondArray = [4, 6, 30];

function mergeSortedArray(firstArray, secondArray) {
  if (!Array.isArray(firstArray) || !Array.isArray(secondArray)) {
    return "Invalid inputs";
  }
  if (firstArray.length === 0) {
    return array2;
  }
  if (secondArray.length === 0) {
    return array1;
  }
  let thirdArray = [...firstArray, ...secondArray].sort((a, b) => a - b);
  console.log(thirdArray);
}

mergeSortedArray(firstArray, secondArray);

//approach 2
function mergeSortedArrayTwo(array1, array2) {
  const mergedArray = [];
  let array1Item = array1[0];
  let array2Item = array2[0];
  let i = 1;
  let j = 1;

  //check input
  if (!Array.isArray(array1) || !Array.isArray(array2)) {
    return "Invalid inputs";
  }
  if (array1.length === 0) {
    return array2;
  }
  if (array2.length === 0) {
    return array1;
  }

  while (array1Item || array2Item) {
    if (!array2Item || array1Item < array2Item) {
      mergedArray.push(array1Item);
      array1Item = array1[i];
      i++;
    } else {
      mergedArray.push(array2Item);
      array2Item = array2[j];
      j++;
    }
  }

  console.log(mergedArray);
}

mergeSortedArrayTwo(firstArray, secondArray);

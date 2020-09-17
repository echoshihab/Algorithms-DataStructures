const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 9];

function bubbleSort(array) {
  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (array[j] < array[i]) {
        let pointer = array[j];
        array[j] = array[i];
        array[i] = pointer;
      }
    }
  }
}

//alternate

function bubbleSortSecond(array) {
  const length = array.length;
  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      if (array[j] > array[j + 1]) {
        //swap numbers
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
}

// bubbleSort(numbers);
// console.log(numbers);
bubbleSortSecond(numbers);
console.log(numbers);

console.log("-------------example O(1)--------------------");
const boxes = [0, 1, 2, 3, 4, 5];

function logFirstTwoBoxes(boxes) {
  console.log(boxes[0] + " O(1)"); //O(1)
  console.log(boxes[1]) + "O(1)"; //O(1)
  console.log(
    "total of 0(2) operations but we round this to O(1) or constant time"
  );
}

logFirstTwoBoxes(boxes); //O(2 but we round this to O(1) or constant time)

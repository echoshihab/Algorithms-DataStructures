//space complextity = 1 since i was only assigned once. so O(1), but time complexity is O(n)

function scExmaple(n) {
  for (let i = 0; i < n.length; i++) {
    console.log("test");
  }
}

scExmaple([1, 2, 3, 4, 5]);

//space complexity - both smpace and time complexity is (O(n))
function scExampleTwo(n) {
  let testArray = [];
  for (let i = 0; i < n.length; i++) {
    testArray[i] = "hi";
  }
  return testArray;
}

scExmapleTwo([1, 2, 3, 4, 5]);

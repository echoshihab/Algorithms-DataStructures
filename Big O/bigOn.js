console.log("-------------example O(n)--------------------");
const nemo = ["Kohn", "Test", "nemo", "magic"];

//find nemo in small array O(4)
function findNemo(array) {
  let t0 = performance.now();
  for (let i = 0; i < array.length; i++) {
    if (array[i] === "nemo") {
      console.log("Found Nemo!");
    }
  }
  let t1 = performance.now();
  console.log(`It took ${t1 - t0} miliseconds to find nemo`);
}

findNemo(nemo);

//find nemo in larger array - O(100)

const large = new Array(100).fill("nemo");

findNemo(large);

//even larger O(1000)
const larger = new Array(1000).fill("nemo");
findNemo(larger);

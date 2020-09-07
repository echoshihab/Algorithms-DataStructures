//Given a number N return the index value of the fibonacci sequence, where the sequence is:
//0,1,1,2,3,5,8,13,21,34,55,89,144...

//the pattern of the sequence is that each value is the sum of the 2 previous values,
// that means that for N=5 => 2+3

function fibonacciIterative(n) {
  let j = 0;
  let k = 0;
  let result = 0;
  for (let i = 0; i <= n; i++) {
    if (i === 0) {
      result = 0;
    }
    if (i === 1) {
      j = 0;
      k = i;
      result = j + k;
    } else {
      result = k + j;
      j = k;
      k = result;
    }
  }

  return result;
}

//alternate approach
function fibonacciAlternativeIterative(n) {
  //O(n-2)
  let arr = [0, 1];
  for (let i = 2; i < n + 1; i++) {
    arr.push(arr[i - 2] + arr[i - 1]);
  }
  return arr[n];
}
console.log(fibonacciAlternativeIterative(10));

console.log(fibonacciIterative(10));

function fibonacciRecursive(n) {
  //O 2^n  -- exponential
  if (n < 2) {
    return n;
  }
  return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

console.log(fibonacciRecursive(10));

//Write two functions that finds the factorial of any number. One should use recursive and
//other should just use a for loop

function findFactorialRecursive(number) {
  debugger;
  if (number === 2) {
    return 2;
  }
  return number * findFactorialRecursive(number - 1);
}

function findFactorialAlternative(number) {
  let answer = 1;
  for (let i = 1; i <= number; i++) {
    answer = answer * i;
  }
  return answer;
}

console.log(findFactorialRecursive(5));
console.log(findFactorialAlternative(7));

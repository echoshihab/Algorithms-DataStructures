//Write two functions that finds the factorial of any number. One should use recursive and
//other should just use a for loop

function findFactorialRecursive(number) {
  let nextNum = number - 1;
  let answer = number;
  if (nextNum == 1) {
    return answer;
  }
  return findFactorialRecursive(nextNum) * answer;
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

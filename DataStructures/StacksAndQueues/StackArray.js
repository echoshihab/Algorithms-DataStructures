class Stack {
  constructor() {
    this.array = [];
  }

  peek() {
    return this.array[this.array.length - 1];
  }

  push(value) {
    this.array.push(value);
    return this;
  }

  pop() {
    this.array.pop();
    return this;
  }
}

let test = new Stack();

test.push(4);
test.push(7);
console.log(test.push(5));
console.log(test.peek());
console.log(test.pop());

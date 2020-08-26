class QueueUsingStack {
  constructor() {
    this.first = [];
    this.last = [];
  }

  peek() {
    if (this.first.length) {
      return this.first[0];
    }
    return this.last[this.last.length - 1];
  }

  enqueue(value) {
    let length = this.first.length;
    for (let i = 0; i < length; i++) {
      this.last.push(this.first.pop());
    }
    this.last.push(value);
    return this;
  }

  dequeue() {
    let length = this.last.length;
    for (let i = 0; i < length; i++) {
      this.first.push(this.last.pop());
    }
    this.first.pop();
    return this;
  }
}

let testQueue = new QueueUsingStack();

testQueue.enqueue("Jess 1");
testQueue.enqueue("James 2");
console.log(testQueue.enqueue("Jody 3"));
console.log(testQueue.dequeue());
console.log(testQueue.peek());

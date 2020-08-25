class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.length = 0;
  }

  peek() {
    return this.first;
  }
  enqueue(value) {
    let newNode = new Node(value);
    if (this.length === 0) {
      this.first = newNode;
      this.last = this.first;
    } else {
      this.last.next = newNode;
      this.last = newNode;
    }

    this.length++;
    return this;
  }
  dequeue() {
    if (!this.first) {
      return null;
    }
    if (this.length === 1) {
      this.first = null;
      this.last = null;
    } else {
      this.first = this.first.next;
    }

    this.length--;
    return this;
  }

  isEmpty() {}
}

let testQueue = new Queue();

//lineup should be - Joy - Matt - Pavel - Samir
testQueue.enqueue("Joy");
testQueue.enqueue("Matt");
testQueue.enqueue("Pavel");
console.log(testQueue.enqueue("Samir"));

//after deque line up should be - Pavel -Samir
testQueue.dequeue();
console.log(testQueue.dequeue());

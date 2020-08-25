class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }

  peek() {
    return this.top;
  }
  push(value) {
    let newNode = new Node(value);
    if (this.length === 0) {
      this.top = newNode;
      this.bottom = newNode;
    } else {
      let prevTop = this.top;
      this.top = newNode;
      this.top.next = prevTop;
    }
    this.length++;
    return this;
  }
  pop() {
    if (this.length === 0) {
      this.top = null;
      this.bottom = null;
      this.length = 0;
    } else {
      this.top = this.top.next;
      this.length--;
      return this;
    }
    this.length++;
    return this;
  }
}

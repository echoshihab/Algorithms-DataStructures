//java script implementation of linked list

class Node {
  constructor(value) {
    (this.value = value), (this.next = null);
  }
}
class LinkedList {
  constructor(value) {
    this.head = {
      value: value,
      next: null,
    };

    this.tail = this.head;
    this.length = 1;
  }
  append(value) {
    const newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
  }

  prepend(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
  }

  printList() {
    const array = [];
    let currentNode = this.head;
    while (currentNode !== null) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    console.log(array);
  }

  insert(index, value) {
    let newNode;
    if (index === 0) {
      this.head.prepend(value);
    }
    if (index === this.length) {
      this.head.append(value);
    }
    if (index !== 0 || index !== this.length) {
      let currentNode = this.head;
      for (let i = 0; i <= index; i++) {
        if (i === index) {
          currentNode.value = value;
          break;
        }
        currentNode = currentNode.next;
      }
    }
    this.length++;
  }
}

const myLinkedList = new LinkedList(10);

myLinkedList.prepend(4);
myLinkedList.prepend(5);
myLinkedList.insert(1, 3);
myLinkedList.printList();

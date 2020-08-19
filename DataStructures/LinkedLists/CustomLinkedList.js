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
    if (index === 0) {
      this.prepend(value);
      return this.printList();
    }
    //check params
    if (index >= this.length) {
      return this.append(value);
    }
    const newNode = new Node(value);
    const leader = this.traverseToIndex(index - 1);
    console.log(leader);
    const holdingPointer = leader.next; //{ value: 10, next: null } } }
    leader.next = newNode; //{value: 3, next: null}
    newNode.next = holdingPointer; //{value: 3 next { value 10, next:null}}
    this.length++;
    return this.printList();
  }
  traverseToIndex(index) {
    let counter = 0;
    let currentNode = this.head;
    while (counter !== index) {
      currentNode = currentNode.next;
      counter++;
    }
    return currentNode;
  }

  // reverse() {
  //   if (!this.head.next) {
  //     return this.head;
  //   }
  //   let first = this.head;
  //   this.tail = this.head;
  //   let second = first.next;
  //   while (second) {
  //     const temp = second.next;
  //     first = second;
  //     second = temp;
  //   }
  //   this.head.next = null;
  //   this.head = first;
  // }

  //alternative:
  // reverse() {
  //   if(!this.head.next){
  //     return this.head;
  //   }
  //   let currentNode = this.head;
  //   let mainPointer = this.head;
  //   this.length = 1;
  //   while (currentNode !== null) {
  //     currentNode = currentNode.next;
  //     if (currentNode !== null) this.prepend(currentNode.value);
  //   }
  //   this.tail = mainPointer;
  //   this.tail.next = null;
  //   return this;

  //[7,5,1,10]
  //[5,7,1,10]
  //[1,5,7],[10]
  //10,1,5,7

  reverse() {
    let first = this.head;
    let tail = this.head;
    let second = first.next;
    while (second) {
      let temp = second.next; //10
      second.next = first; //1=>5=>7
      first = second; //1=>5=7
      second = temp; //10
    }

    //so the progression is
    //first iteration = first = [5=>7], second =[1,10]
    //second iteration  first = [1=>5=>7] second=[10]
    //last iteration = first = [10] second=[1=>5=>7]

    this.head.next = null; //since this head is still at 7 at this point, make the next null
    this.head = first; // and now point the head to first
  }

  remove(index) {
    let leader;
    if (index === 0) {
      this.head = this.head.next;
      this.length--;
      return this.printList();
    }
    if (index === this.length - 1) {
      leader = this.traverseToIndex(index - 1);
      leader.next = null;
      this.length--;
      return this.printList();
    }

    leader = this.traverseToIndex(index - 1);
    let follower = this.traverseToIndex(index + 1);
    //alternative method
    //const unwantedNode = leader.next;
    //leader.next = unwantedNode.next;
    leader.next = follower;
    return this.printList();
  }
}

const myLinkedList = new LinkedList(10);

myLinkedList.prepend(1);
myLinkedList.prepend(5);
myLinkedList.prepend(7);
myLinkedList.reverse();
myLinkedList.printList();

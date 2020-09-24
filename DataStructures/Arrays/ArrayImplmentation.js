class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }
  get(index) {
    return this.data[index];
  }
  set(index, value) {
    this.data[index] = value;
  }

  push(value) {
    this.data[this.length] = value;
    this.length++;
  }
  pop() {
    let toBeDeleted = this.data[this.length - 1];
    delete this.data[this.length - 1];
    this.length--;
    return toBeDeleted;
  }
  insert(index, value) {
    if (index < 0 || index > this.length) {
      console.log("Index out of bounds");
      return false;
    } else if (index == this.length) {
      this.push(value);
    } else {
      this.length++;
      let i = this.length - 1;
      while (i > index) {
        this.data[i] = this.data[i - 1];
        i--;
      }
      this.data[index] = value;
    }
  }
  delete(index) {
    if (index > this.length || index < 0) {
      console.log("Invalid Index");
      return false;
    } else if (index === this.length) {
      this.pop();
    } else {
      let i = index;
      while (i < this.length - 1) {
        this.data[i] = this.data[i + 1];
        i++;
      }
      delete this.data[this.length - 1];
      this.length--;
    }
  }
}

let test = new MyArray();
test.push(4);
test.push(2);
test.insert(1, 5);
test.insert(2, 9);

console.log(test.data);
test.set(1, 6);
console.log(test.data);
test.delete(0);
test.delete(1);
console.log(test.data);

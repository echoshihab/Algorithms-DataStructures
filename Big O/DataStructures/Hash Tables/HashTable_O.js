let user = {
  age: 150,
  name: "Dracula",
  magic: true,
  spell: function () {
    console.log("Dracula mesmerized you");
  },
};

console.log(user.age); // this is O(1);

//with collision this slows down to //0(n/k) where k is size of hash table
//and thus this becomes O(n) after removal of constants

const strings = ["a", "b", "c", "d"];
//in a 32 bit system this takes 4*4 = 16 bytes of storage

//javascript methods
strings.push("e"); //O(1)

//pop
strings.pop(); //O(1)

//unshift
strings.unshift("z"); //O(n) = we are looping over the array to assign indexes

strings.splice(2, 0, "alien"); //(O(n))

let arr = strings[2]; //O(1)

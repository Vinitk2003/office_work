//array
 // start with 0 index linear
// let marks = ["vinit","vaidik","vaibhav","vasu","vapi","vasudev"]
// console.log(marks);
// console.log(marks.length);
// console.log(typeof(marks))
// marks[2] = "viku"
// console.log(marks);

// //looping in an array
// for (let i = 0; i < marks.length; i++) {
//     console.log(marks[i]);
// }

// //for of
// for (let mark of marks) {
//     console.log(mark.toUpperCase());
// }

let marks = [ 89,76,98,76,76]

let sum = 0;

for (let val of marks){
    sum += val;
}

let avg = sum / marks.length;
console.log(avg);
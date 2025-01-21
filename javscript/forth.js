// condeitional statement
// if statement
// let age =  18;
// if (age >= 18) {
//     console.log("You are an adult");
// }

// if (age < 18) {
//     console.log("You are a minor");
// }

//if - else statement
let mode = "light";
let color;

if (mode == "dark"){
    color = "black;"
}else {
    color = "white";
}

console.log(color)

//odd or even
let number = 10;
if (number % 2 == 0) {
    console.log("The number is even");
} else {
     console.log("The number is odd");
     }

//else-if statement
let score = 50;
if (score >= 80) {
    console.log("Grade A");
    } else if (score >= 70) {
        console.log("Grade B");
        } else if (score >= 60) {
            console.log("Grade C");
        }else {
            console.log("Grade D");
        }

 //switch statement
let day = "Friday";
 switch (day) {
     case "Monday":
         console.log("Today is Monday");
         break;
         case "Tuesday":
             console.log("Today is Tuesday");
             break;
         case "Wednesday":
             console.log("Today is Wednesday");
             break;
         case "Thursday":
             console.log("Today is Thursday");
             break;
         case "Friday":
             console.log("Today is Friday");
             break;
                 default:
             console.log("Invalid day");
             break;
                }
  //ternary operator
  let age = 25;
  let result = age >= 18 ? "Adult" : "Minor";
  console.log(result);
 
  //for loop
  for (let i = 0; i < 5; i++) {
    console.log(i);
    }


    



                                    

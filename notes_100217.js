// console.log("Hello, world!")   # print like python

// alert("Hello") # pops up notification

// VARIABLES

// var someName;   # name a variable like in python name = name()
// var myName = 'Jeff'  #sets variables
// console.log(myName)  #prints variable

// GREET Function
// function greeting(name) {
//     console.log("Hello, " + name + "!")
// }
//
// greeting(myName)

// INSERT TO HTML
// <script src"file.js"></script>

//EXAMPLE
// "use strict";  # put at the top of the js page. helpful for debugging.

// var myName = "Jeff";
//
// function greeting(name) {
//     alert("hello " + name + "!")
// }

// DATA TYPES

// int = 123
// float = 0.2
// string "str"
// array = ["apple", "orange"]
// json = {"key": "value"}

// FOR LOOP
// var fruit = ["apple", "orange", "banana"];
//
// for (var i = 0; i < fruit.length; i++) {
//     console.log(fruit[i])
// } # for a while loops are somewhat combined in js.

// EQUAL SIGNS
// var thisThing = 1 == '1'  # this returns true
// var thisThing = 1 === '1' # this returns False


//CONDITIONALS
// function greeting(name) {
//     if (name === "Chris") {
//         alert("hello " + name + "! something extra")
//     } else if (name === "shari" || name === "chelsea") {
//         console.log("welcome to the place here.", name, "... ")
//     } else {
//         console.log("it's a nice day to see you " + name + ". ")
//     }
// }

//INPUT FROM SUBMIT BUTTON
// document.getElementById('submit').addEventListener('click', function () {
//     event.preventDefault();
//     color = document.getElementById('colorChoice').value;
//     console.log(color)
// })

// ADD HTML TO AN ID
// document.getElementById("messageBox").innerHTML = "You picked " + color + ". Good job!!job"

// INTEGER FORMATTING.
// var p = prompt("enter a number to add two to:  ")
// var number = parseInt(p) + 2;
// console.log(number)

//STRING FORMATTING
// var number = parseInt(p) + 2;
// var stri = String(number)

// Global objects: string, number, date,

//RANDOM NUMBER
// var r_num = Math.random();
// console.log(r_num)  #  Prints a random number between 0 and 1.
//
// var r_num = Math.floor((Math.random() * 10) + 1);

//PROTOTYPE METHODS
// var name = "Chris";
// console.log(name.startsWith("C"));

//LODASH FILTER
// var thing = _.filter([1, 2, 3, 4, 5, 6], function (num) {
//     return num % 2 === 0;
// })

// // SIMILAR TO CLASSES IN PYTHON
// var animalNoises = {
//     name: null,
//     age: 0;
//     makeDogNoise: function () {
//         return "bork!";
//     },
//     makeCatNoise: function () {
//
//         return "Meow!"
//     }
// };
// console.log(animalNoises.makeCatNoise());
// console.log(animalNoises.makeDogNoise());


//OBJECTS
// var bankAccount = {
//     balance: 0;
//     deposit: function (amount) {
//         this.balance += amount;
//     }
// }
//
//SIMILAR TO SELF
// "use strict";
//
//
// $('.colorBox').click(function () {
//     $(this).css('backgroundColor', 'red')
// });
//
//
// $('.colorBox').click(function () {
//     $(this).children().css('backgroundColor', 'red')
// });

var timer = setInterval( function () {
    console.log("Hi");
}, 500);

clearInterval(timer) # clears the variable of the

var timer = setInterval( function () {
    $("#message").html("This has ran, " + count + "times. ")
}, 500);

clearInterval(timer) # clears the variable of the



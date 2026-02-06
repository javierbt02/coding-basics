const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

console.log("Welcome to the temperature converter.");

let scale = null;
let fahrenheit = null;
let celsius = null;
let resultftoc = null;
let resultctof = null;
const array = ["c", "f", "x"];

function question2(){
    rl.question("Now write the temperature you want to convert in Fahrenheit degrees: \n", (ans_fahrenheit) => {

        fahrenheit = Number(ans_fahrenheit);

        if (Number.isNaN(fahrenheit)) {
            console.log("Please try again.");
            question2();
            }
        else {
            resultftoc = (fahrenheit-32)*(5/9);
            console.log(`The temperature you inserted in Fahrenheit degrees: ${fahrenheit}. \nConvertion to Celsius degrees: ${resultftoc}.`);
            question1();
            }
            })
            }

function question3(){
    rl.question("Now write the temperature you want to convert in Celsius degrees: \n", (ans_celsius) => {

        celsius = Number(ans_celsius);

        if (Number.isNaN(celsius)) {
            console.log("Please try again.");
            question3();
            }
        else {
            resultctof = (celsius*9/5)+32;
            console.log(`The temperature you inserted in Celsius degrees: ${celsius}. \nConvertion to Fahrenheit degrees: ${resultctof}.`);
            question1();
            }
            })
            }

function question1() {
    rl.question("Please, write down what temperature scale you want to convert to (c for celsius/f for fahrenheit/x to exit): \n", (ans_scale) => {
    
    scale = ans_scale.toLowerCase();

    if (scale.length !== 1 || !array.includes(scale)){
        console.log("Please try again.");
        question1();
    }

    else if (scale == "c") {
        question2();
        }
        
    else if (scale == "f") {
        question3();
        }

    else {
        console.log("Thank you for using this program.");
        rl.close();
        };
    })

    }

question1();
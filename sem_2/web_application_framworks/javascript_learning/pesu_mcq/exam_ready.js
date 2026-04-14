/******************************************************
 🔥 1. VARIABLES & DATA TYPES
******************************************************/

var a = 10;        // old way (function scope)
let b = 20;        // modern (block scope)
const c = 30;      // constant (cannot change)

let name = "Piyush";   // String
let isStudent = true;  // Boolean
let x = null;          // Null
let y;                 // Undefined

console.log(typeof name); // string


/******************************************************
 🔥 2. USER INPUT (IMPORTANT FOR EXAM)
******************************************************/

// Browser input
let userInput = prompt("Enter a number:");
console.log(userInput);

// Convert to number
let num = Number(userInput);


/******************************************************
 🔥 3. OPERATORS
******************************************************/

let sum = 5 + 3;
let diff = 5 - 3;
let mul = 5 * 3;
let div = 5 / 3;
let mod = 5 % 3;

console.log(5 == "5");   // true (loose equality)
console.log(5 === "5");  // false (strict equality)


/******************************************************
 🔥 4. IF-ELSE CONDITIONS
******************************************************/

let age = 18;

if (age >= 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}

// Ternary Operator
let result = (age >= 18) ? "Adult" : "Minor";


/******************************************************
 🔥 5. LOOPS
******************************************************/

// FOR LOOP
for (let i = 1; i <= 5; i++) {
    console.log(i);
}

// WHILE LOOP
let i = 1;
while (i <= 5) {
    console.log(i);
    i++;
}

// DO-WHILE
let j = 1;
do {
    console.log(j);
    j++;
} while (j <= 5);


/******************************************************
 🔥 6. FUNCTIONS
******************************************************/

// Normal function
function add(a, b) {
    return a + b;
}

// Arrow function
const multiply = (a, b) => a * b;

console.log(add(2,3));
console.log(multiply(2,3));


/******************************************************
 🔥 7. ARRAYS
******************************************************/

let arr = [10, 20, 30];

// Access
console.log(arr[0]);

// Add elements
arr.push(40);
arr.unshift(5);

// Remove
arr.pop();
arr.shift();

// Loop array
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

// forEach
arr.forEach(val => console.log(val));


/******************************************************
 🔥 8. STRINGS
******************************************************/

let str = "hello world";

console.log(str.length);
console.log(str.toUpperCase());
console.log(str.includes("hello"));


/******************************************************
 🔥 9. OBJECTS
******************************************************/

let student = {
    name: "Piyush",
    age: 20,
    marks: 90
};

console.log(student.name);

// Add property
student.city = "Bangalore";


/******************************************************
 🔥 10. IMPORTANT ARRAY METHODS (EXAM FAVORITE)
******************************************************/

let nums = [1, 2, 3, 4];

// map (transform)
let doubled = nums.map(n => n * 2);

// filter
let even = nums.filter(n => n % 2 === 0);

// reduce
let total = nums.reduce((sum, n) => sum + n, 0);

console.log(doubled, even, total);


/******************************************************
 🔥 11. DOM (VERY IMPORTANT)
******************************************************/

// Select element
let element = document.getElementById("myId");

// Change content
element.innerText = "Hello";

// Event
element.onclick = function() {
    alert("Clicked!");
};


/******************************************************
 🔥 12. EVENTS
******************************************************/

document.addEventListener("click", () => {
    console.log("Page clicked");
});


/******************************************************
 🔥 13. SET TIMEOUT & INTERVAL
******************************************************/

setTimeout(() => {
    console.log("Runs once after 2 sec");
}, 2000);

setInterval(() => {
    console.log("Runs every 2 sec");
}, 2000);


/******************************************************
 🔥 14. ERROR HANDLING
******************************************************/

try {
    let x = y; // error
} catch (err) {
    console.log("Error handled");
}


/******************************************************
 🔥 15. PROMISES (IMPORTANT THEORY + CODE)
******************************************************/

let promise = new Promise((resolve, reject) => {
    let success = true;

    if (success) resolve("Done");
    else reject("Failed");
});

promise.then(res => console.log(res))
       .catch(err => console.log(err));


/******************************************************
 🔥 16. ASYNC-AWAIT
******************************************************/

async function fetchData() {
    return "Data received";
}

async function run() {
    let data = await fetchData();
    console.log(data);
}

run();


/******************************************************
 🔥 17. LOCAL STORAGE
******************************************************/

localStorage.setItem("name", "Piyush");
console.log(localStorage.getItem("name"));


/******************************************************
 🔥 18. TYPE CONVERSION
******************************************************/

let n1 = "10";
let n2 = Number(n1);   // string → number

let n3 = 20;
let n4 = String(n3);   // number → string


/******************************************************
 🔥 19. IMPORTANT SMALL QUESTIONS (EXAM)
******************************************************/

// Reverse a string
let s = "hello";
let rev = s.split("").reverse().join("");
console.log(rev);

// Check palindrome
let word = "madam";
let isPal = word === word.split("").reverse().join("");
console.log(isPal);

// Largest number in array
let arr2 = [5, 2, 9, 1];
let max = Math.max(...arr2);
console.log(max);


/******************************************************
 🔥 END OF FULL REVISION
******************************************************/
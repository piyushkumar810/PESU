// Sample input
let text = "User: Piyush123, Email: piyush@gmail.com, Age: 21";

// 1️⃣ Extract numbers (like age)
let numbers = text.match(/\b\d+\b/g);

// 2️⃣ Check if username starts with capital letter
let username = "Piyush123";
let isValidUsername = /^[A-Z]\w*/.test(username);

// 3️⃣ Simple email validation
let email = "piyush@gmail.com";
let emailRegex = /^[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,}$/;
let isValidEmail = emailRegex.test(email);

// Output
console.log("Numbers:", numbers);
console.log("Valid Username:", isValidUsername);
console.log("Valid Email:", isValidEmail);
// ===============================
// 1. let, const, Template literals
// ===============================
let age = 21;
const name = "Piyush";

console.log(`My name is ${name} and I am ${age} years old`);


// ===============================
// 2. Default Parameters
// ===============================
function greet(user = "Guest") {
  console.log(`Hello ${user}`);
}
greet();
greet(name);


// ===============================
// 3. Spread Operator
// ===============================
let arr1 = [1, 2];
let arr2 = [...arr1, 3, 4];
console.log("Spread:", arr2);


// ===============================
// 4. Destructuring
// ===============================
let numbers = [10, 20, 30];
let [a, b, c] = numbers;

let personObj = { pname: "Piyush", page: 21 };
let { pname, page } = personObj;

console.log("Destructuring:", a, b, c, pname, page);


// ===============================
// 5. Classes + Arrow Function
// ===============================
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet = () => {
    console.log(`Hi, I'm ${this.name}`);
  };
}

let p1 = new Person("Piyush", 21);
p1.greet();


// ===============================
// 6. ES6 Modules (SIMULATION)
// ===============================
// (In real case: export/import from files)
function add(x, y) {
  return x + y;
}
console.log("Module Function:", add(2, 3));


// ===============================
// 7. Set (ES6 Collection)
// ===============================
let set = new Set([1, 2, 2, 3, 3]);
console.log("Set:", set);


// ===============================
// 8. Map Object
// ===============================
let map = new Map();
map.set("name", "Piyush");
map.set("age", 21);

console.log("Map:", map.get("name"), map.get("age"));


// ===============================
// 9. Rest Operator
// ===============================
function total(...nums) {
  return nums.reduce((sum, n) => sum + n, 0);
}
console.log("Rest:", total(1, 2, 3, 4));


// ===============================
// 10. Optional Chaining + Nullish
// ===============================
let user = {};
console.log("Optional:", user?.address?.city ?? "No City");


// ===============================
// 11. Promise
// ===============================
let promise = new Promise((resolve, reject) => {
  let success = true;

  setTimeout(() => {
    if (success) {
      resolve("Task Completed");
    } else {
      reject("Task Failed");
    }
  }, 1000);
});

promise
  .then(result => console.log("Promise:", result))
  .catch(error => console.log(error));


// ===============================
// FINAL COMBINED FLOW
// ===============================
function main(...nums) {
  let sum = nums.reduce((a, b) => a + b);

  let newArr = [...nums, sum];

  let uniqueValues = new Set(newArr);

  let dataMap = new Map();
  dataMap.set("sum", sum);

  let obj = { data: { value: sum } };

  console.log("\nFINAL OUTPUT:");
  console.log("Numbers:", nums);
  console.log("Sum:", sum);
  console.log("Spread:", newArr);
  console.log("Set:", uniqueValues);
  console.log("Map:", dataMap.get("sum"));
  console.log("Optional:", obj?.data?.value ?? "No Value");
}

main(1, 2, 3, 4);
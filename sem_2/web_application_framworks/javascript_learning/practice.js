let a=[10,29,30,40];
for(let i of a){
    console.log(i);
}

for(let i in a){
    console.log(i)
}

let c=0b101;
console.log(c);


// Write an arrow function to return even numbers from an array

const getarray = (arr)=>{
    return arr.filter(num => num%2===0)
}
arr=[10,3,567,3,5,235,566,4,23,346,9]
console.log(getarray(arr));

/*
const square = x => x * x;   // auto return

const square2 = x => { 
    return x * x;            // needed
}; 
*/

// --------------------------------------------------------------------------------

// 🔹 2. Getters and Setters (SHORT + DEEP)
// ❓ What?
// Used to control access to object properties

// ✅ Example:
class Person {
  constructor(name){
    this._name = name;
  }

  get name(){
    return this._name;
  }

  set name(newName){
    this._name = newName;
  }
}

let p = new Person("Piyush");
console.log(p.name);   // getter
p.name = "Kumar";      // setter
console.log(p.name);
/*
🔑 Key Understanding:
get → read value
set → update value
_name → private-like variable
⚠️ Important MCQ Point:
Getter is called like property → p.name (NOT p.name())
🎯 Why use?
Validation
Encapsulation
Controlled access
*/


// 🔹 3. Promises (SHORT + DEEP)
// ❓ What?

// Promise = future result of async operation
// ✅ Basic Example:
let promise = new Promise((resolve, reject) => {
  let success = true;

  if(success){
    resolve("Success");
  } else {
    reject("Error");
  }
});

promise.then(res => console.log(res))
       .catch(err => console.log(err));

/*
🔑 States:
Pending → initial
Resolved (fulfilled) → success
Rejected → error
🔥 Your Given Code Explained:
new Promise((res,rej)=> res("done"));

👉 Meaning:

Promise created
Immediately resolved
"done" is returned
🎯 Flow:
Create → Resolve → then() runs
⚠️ Important MCQ Points:
.then() → success
.catch() → error
Promise is asynchronous
*/


// ----------------------------- mcqs
// ❓3 JSX Error
/*
return (
  <h1>Hello</h1>
  <p>World</p>
);

👉 Answer:
❌ Error: Multiple root elements
✔ Fix:

return (
  <>
    <h1>Hello</h1>
    <p>World</p>
  </>
);
*/

// -------------------------------------------------
// ❓5 Conditional Rendering
const x = 15;
<h1>{x < 10 ? "Hello" : "Bye"}</h1>;

// 👉 Answer:
// ✔ Output: Bye


//----------------------------------------------------
// ❓9 Props Access
class A extends React.Component {
  render() {
    return <h1>{this.props.name}</h1>;
  }
}

// 👉 Answer:
// ✔ Correct way to access props in class


/*
❓5

Output?

<h1>{true}</h1>

A) true
B) false
C) blank
D) error

👉 Answer: C
✔ Boolean doesn’t render

❓6

Which is valid?
A) <h1 class="a">
B) <h1 className="a">
C) <h1 classname="a">
D) <h1 ClassName="a">

👉 Answer: B

❓7

What happens if key is missing in list?
A) Error
B) Warning
C) Crash
D) No rendering

👉 Answer: B
*/
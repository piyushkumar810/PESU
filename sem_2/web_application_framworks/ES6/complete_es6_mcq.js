/*
🔥 FINAL 30 MCQs

Q1 (Default Parameter)
function f(x = 5){
  return x;
}
console.log(f(null));

a) 5
b) null
c) undefined
d) error

✅ Answer: b) null
👉 default works only for undefined

Q2 (let scope)
for(let i=0;i<2;i++){}
console.log(i);

a) 0
b) 1
c) undefined
d) error

✅ Answer: d) error
👉 let is block scoped

Q3 (var scope)
for(var i=0;i<2;i++){}
console.log(i);

a) 1
b) 2
c) undefined
d) error

✅ Answer: b) 2
👉 var is global

Q4 (Arrow Function)
const f = x => {x*2};
console.log(f(5));

a) 10
b) undefined
c) error
d) 5

✅ Answer: b) undefined
👉 missing return

Q5 (Arrow shortcut)
const f = x => x*2;
console.log(f(5));

a) 10
b) undefined
c) error
d) 5

✅ Answer: a) 10

Q6 (Template Literal)
let a = 5;
console.log(`Value: ${a+5}`);

a) Value: 5
b) Value: 10
c) Value: a+5
d) error

✅ Answer: b) Value: 10

Q7 (Spread)
let a = [1,2];
let b = [...a,3];
console.log(b);

a) [1,2,3]
b) [[1,2],3]
c) [3,1,2]
d) error

✅ Answer: a)

Q8 (Rest)
function f(...a){
  return a.length;
}
console.log(f(1,2,3));

a) 1
b) 2
c) 3
d) error

✅ Answer: c)

Q9 (Destructuring)
let [a,b] = [1];

a) a=1,b=1
b) a=1,b=undefined
c) error
d) null

✅ Answer: b)

Q10 (Object Destructuring)
let obj = {x:10};
let {y} = obj;

a) y=10
b) y=undefined
c) error
d) null

✅ Answer: b)

Q11 (for...of)
for(let x of [1,2]){
  console.log(x);
}

a) 0 1
b) 1 2
c) error
d) undefined

✅ Answer: b)

Q12 (for...in)
for(let x in [1,2]){
  console.log(x);
}

a) 1 2
b) 0 1
c) error
d) undefined

✅ Answer: b)

Q13 (== vs ===)
console.log(0 == false, 0 === false);

a) true true
b) true false
c) false true
d) false false

✅ Answer: b)

Q14 (Logical)
console.log("" || "hi");

a) ""
b) hi
c) false
d) undefined

✅ Answer: b)

Q15 (typeof)
console.log(typeof null);

a) null
b) object
c) undefined
d) error

✅ Answer: b)

Q16 (Map)
let m = new Map();
m.set(1,"a");
m.set(1,"b");
console.log(m.get(1));

a) a
b) b
c) undefined
d) error

✅ Answer: b)
👉 key overwritten

Q17 (Promise)
new Promise((res)=>res(5))
.then(x=>console.log(x));

a) 5
b) undefined
c) error
d) promise

✅ Answer: a)

Q18 (Promise state)

👉 resolve() means?

a) error
b) success
c) pending
d) cancel

✅ Answer: b)

Q19 (Class)
class A{}
console.log(typeof A);

a) class
b) object
c) function
d) undefined

✅ Answer: c)

Q20 (instanceof)
class A{}
let a = new A();
console.log(a instanceof A);

a) true
b) false
c) error
d) undefined

✅ Answer: a)

Q21 (Getter)
class A{
  get x(){ return 5; }
}
let a = new A();
console.log(a.x);

a) 5
b) undefined
c) error
d) function

✅ Answer: a)

Q22 (Setter)
class A{
  set x(v){ this._x = v; }
}
let a = new A();
a.x = 10;

👉 Works?

a) yes
b) no
c) error
d) undefined

✅ Answer: a)

Q23 (Module)

👉 Which is correct?

a) import add from
b) import {add}
c) require(add)
d) include(add)

✅ Answer: b)

Q24 (Binary)
console.log(0b101);

a) 5
b) 101
c) error
d) 3

✅ Answer: a)

Q25 (Octal)
console.log(0o10);

a) 10
b) 8
c) error
d) 2

✅ Answer: b)

Q26 (Ternary)
console.log(5>3 ? "yes":"no");

a) yes
b) no
c) error
d) undefined

✅ Answer: a)

Q27 (Dynamic typing)
let x = 5;
x = "hi";

👉 x is?

a) number
b) string
c) both
d) error

✅ Answer: c)

Q28 (Arrow this)

👉 Arrow function has its own this?

a) yes
b) no
c) sometimes
d) error

✅ Answer: b)

Q29 (Rest rule)

👉 Rest parameter must be?

a) first
b) last
c) middle
d) anywhere

✅ Answer: b)

Q30 (Spread)

👉 Spread does?

a) collect
b) expand
c) delete
d) sort

✅ Answer: b)
*/
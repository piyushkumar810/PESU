/*
🔥 MOST IMPORTANT OUTPUT QUESTIONS
1️⃣ Basic Output
console.log("Start");

setTimeout(() => {
    console.log("Inside Timeout");
}, 0);

console.log("End");
✅ Output
Start
End
Inside Timeout

👉 Even 0ms delay is not immediate

2️⃣ Loop with var
for (var i = 1; i <= 3; i++) {
    setTimeout(() => {
        console.log(i);
    }, 1000);
}
✅ Output
4
4
4

👉 Why?

var is function scoped
Loop ends → i = 4
All callbacks print same value
3️⃣ Loop with let
for (let i = 1; i <= 3; i++) {
    setTimeout(() => {
        console.log(i);
    }, 1000);
}
✅ Output
1
2
3

👉 let creates new variable each iteration

4️⃣ Increasing Delay
for (let i = 1; i <= 3; i++) {
    setTimeout(() => {
        console.log(i);
    }, i * 1000);
}
✅ Output (after delays)
1  (after 1s)
2  (after 2s)
3  (after 3s)
5️⃣ Mixed Sync + Async
console.log("A");

setTimeout(() => console.log("B"), 1000);

console.log("C");
✅ Output
A
C
B
6️⃣ Nested setTimeout
setTimeout(() => {
    console.log("1");

    setTimeout(() => {
        console.log("2");
    }, 0);

}, 0);
✅ Output
1
2
7️⃣ Trick Question (IMPORTANT)
setTimeout(() => console.log("A"), 0);
console.log("B");
setTimeout(() => console.log("C"), 0);
✅ Output
B
A
C

👉 Order of registration matters

⚡ SUPER IMPORTANT EXAM THEORY POINTS
JS is single-threaded
Uses event loop
setTimeout is asynchronous
Even 0ms → delayed execution
var vs let → BIG difference in loops
🎯 HOW TO WRITE IN EXAM (5 MARK PERFECT)

Write:

Code
Output
Reason:
synchronous first
async later
event loop explanation 
*/
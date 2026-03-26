'''🎯 SET 2: GATE-Level MCQs

❓ Q1 (Concept Trap)

Which statement is TRUE about asymptotic analysis?

A) It gives exact running time
B) It depends on machine and compiler
C) It focuses on growth rate of time with input size
D) It works only for small inputs

✅ Answer: C
💡 Explanation:
Asymptotic ≠ exact time ❌
Machine independent ✔
Focus = growth rate

👉 Exam trap: Many choose A (wrong)



❓ Q2 (Formula-Based)

If an algorithm performs 5n² + 3n + 10 operations, its asymptotic complexity is:

A) O(n)
B) O(n²)
C) O(n³)
D) O(log n)

✅ Answer: B
💡 Explanation:

👉 Ignore constants & lower terms
👉 Dominant term = n²



❓ Q3 (Very Tricky)

Which grows faster as n → ∞?

A) n log n
B) n¹·⁵
C) n²
D) 2ⁿ

✅ Answer: D
💡 Explanation:

👉 Exponential beats all polynomial functions

Order:
n log n < n¹·⁵ < n² < 2ⁿ



❓ Q4 (Scenario-Based)

An algorithm takes:

1 sec for n = 100
4 sec for n = 200

What is the likely complexity?

A) O(n)
B) O(n²)
C) O(log n)
D) O(2ⁿ)

✅ Answer: B
💡 Explanation:

n doubles → time becomes 4×
👉 Indicates quadratic (n²)



❓ Q5 (Basic Operation Concept)

The running time of an algorithm mainly depends on:

A) Number of variables
B) Number of lines of code
C) Number of times basic operation executes
D) Programming language

✅ Answer: C
💡 Explanation:

👉 Core idea from slides
👉 Count basic operation frequency



❓ Q6 (VERY IMPORTANT TRAP)

Which is TRUE?

A) Best case gives upper bound
B) Worst case gives lower bound
C) Worst case gives upper bound
D) Average case gives exact bound

✅ Answer: C
💡 Explanation:
Worst case → maximum → upper bound ✔
Best case → minimum → lower bound ✔



❓ Q7 (Growth Comparison)

Which is smallest for large n?

A) n²
B) log n
C) √n
D) n

✅ Answer: B
💡 Explanation:

Order:
log n < √n < n < n²

👉 log n is smallest



❓ Q8 (Advanced Order)

Which grows faster?

A) n² log n
B) n³
C) n log n
D) n²

✅ Answer: B
💡 Explanation:

👉 Compare dominant power:
n³ > n² log n > n² > n log n



❓ Q9 (Amortized Concept)

Which statement is TRUE about amortized analysis?

A) It analyzes worst case only
B) It analyzes single operation
C) It gives average cost over sequence of operations
D) It ignores costly operations

✅ Answer: C
💡 Explanation:

👉 Key idea:
Expensive operations spread over many cheap ones



❓ Q10 (Real GATE Style)

Which of the following is NOT affected in asymptotic analysis?

A) Input size
B) Growth rate
C) Machine speed
D) Number of operations

✅ Answer: C
💡 Explanation:

👉 Machine speed ignored
👉 Focus only on growth



❓ Q11 (Mixed Concept)

If T(n) = 3n log n + 5n, then:

A) O(n)
B) O(n log n)
C) O(n²)
D) O(log n)

✅ Answer: B
💡 Explanation:

👉 Dominant term = n log n



❓ Q12 (Hard Scenario)

An algorithm has:

Worst case: O(n²)
Best case: O(n)

Which is TRUE?

A) Algorithm always runs in O(n)
B) Algorithm always runs in O(n²)
C) Running time depends on input
D) Worst case is useless

✅ Answer: C
💡 Explanation:

👉 Time depends on input
👉 That’s why multiple cases exist
'''
# KMP Algorithm
# Step 1: Compute Failure Function (LPS Array)

def compute_failure_function(pattern):
    m = len(pattern)
    F = [0] * m

    k = 0

    for j in range(1, m):

        while k > 0 and pattern[k] != pattern[j]:
            k = F[k - 1]

        if pattern[k] == pattern[j]:
            k += 1

        F[j] = k

    return F


# KMP search
def kmp_search(text, pattern):

    n = len(text)
    m = len(pattern)

    F = compute_failure_function(pattern)

    j = 0

    for i in range(n):

        while j > 0 and pattern[j] != text[i]:
            j = F[j - 1]

        if pattern[j] == text[i]:
            j += 1

        if j == m:
            return i - m + 1

    return -1


text = "ZZABCZZ"
pattern = "ABC"

result = kmp_search(text, pattern)

if result != -1:
    print("Pattern found at index", result)
else:
    print("Pattern not found")


# explanation
'''
KMP ALGORITHM EXAMPLE

Text = "ZZABCZZ"
Pattern = "ABC"

---

## STEP 1: COMPUTE FAILURE FUNCTION (LPS ARRAY)

Pattern:

A B C
0 1 2

Initialize:

F[0] = 0
k = 0

Current F:

[0, 0, 0]

---

j = 1

Compare:

P[k] = P[0] = A
P[j] = P[1] = B

A ≠ B

No match

F[1] = 0

Current F:

[0, 0, 0]

---

j = 2

Compare:

P[k] = P[0] = A
P[j] = P[2] = C

A ≠ C

No match

F[2] = 0

Current F:

[0, 0, 0]

---

Final Failure Function:

F = [0, 0, 0]

---

## STEP 2: KMP SEARCH TRACE

Text    = Z Z A B C Z Z
Index   = 0 1 2 3 4 5 6

Pattern = A B C

Initial:

j = 0

---

i = 0

Text Character    = Z
Pattern Character = A

A ≠ Z

No match

j = 0

---

i = 1

Text Character    = Z
Pattern Character = A

A ≠ Z

No match

j = 0

---

i = 2

Text Character    = A
Pattern Character = A

A = A ✓

j = 1

---

i = 3

Text Character    = B
Pattern Character = B

B = B ✓

j = 2

---

i = 4

Text Character    = C
Pattern Character = C

C = C ✓

j = 3

Since:

j = m = 3

Pattern found.

Return:

i - m + 1

= 4 - 3 + 1

= 2

---

## OUTPUT

Pattern found at index 2

'''
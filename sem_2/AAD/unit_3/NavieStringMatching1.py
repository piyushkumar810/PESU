def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0

        while j < m and pattern[j] == text[i + j]:
            j += 1

        if j == m:
            return i

    return -1


# Example
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

result = naive_string_matching(text, pattern)

if result != -1:
    print("Pattern found at index:", result)
else:
    print("Pattern not found")


# ---------------------- explanation
'''
NAIVE STRING MATCHING

Text = "ZZABCZZ"
Pattern = "ABC"

Text length (n) = 7
Pattern length (m) = 3

Possible positions = n - m = 4
So, i = 0, 1, 2, 3, 4

--------------------------------------------------

i = 0

ABC
ZZABCZZ

Compare:
A ≠ Z

✗ Not matched

--------------------------------------------------

i = 1

 ABC
ZZABCZZ

Compare:
A ≠ Z

✗ Not matched

--------------------------------------------------

i = 2

  ABC
ZZABCZZ

Compare:
A = A ✓
B = B ✓
C = C ✓

✓ Pattern found at index 2

--------------------------------------------------

i = 3

   ABC
ZZABCZZ

Compare:
A ≠ B

✗ Not matched

--------------------------------------------------

i = 4

    ABC
ZZABCZZ

Compare:
A ≠ C

✗ Not matched

--------------------------------------------------

Algorithm Conclusion:

The pattern "ABC" is found in the text "ZZABCZZ"
at index 2.

Time Complexity:
Best Case  : O(n)
Worst Case : O(n × m)

where,
n = length of text
m = length of pattern
'''
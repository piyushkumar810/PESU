'''
1. Valid Parentheses ⭐⭐⭐⭐⭐
Problem

Given:

"()[]{}"

Check whether the brackets are correctly matched.

Examples:

"()"       → True
"()[]{}"   → True
"(]"       → False
"([)]"     → False
"{[]}"     → True
'''


def isValid(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)

    return not stack
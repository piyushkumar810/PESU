# ============================================================
# LeetCode 13 - Roman to Integer
# ============================================================
#
# QUESTION:
# Roman numerals use these 7 symbols:
#
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
#
# Given a Roman numeral string, convert it into an integer.
#
# Examples:
#
# "III"   → 3
# "LVIII" → 58
# "MCMXCIV" → 1994
#
# IMPORTANT RULE:
#
# Normally, Roman values are added:
#
# XII = 10 + 1 + 1 = 12
#
# But if a smaller value comes BEFORE a larger value,
# we subtract the smaller value:
#
# IV = 5 - 1 = 4
# IX = 10 - 1 = 9
# XL = 50 - 10 = 40
# XC = 100 - 10 = 90
# CD = 500 - 100 = 400
# CM = 1000 - 100 = 900
#
# Therefore:
#
# Current value < Next value → SUBTRACT
# Current value >= Next value → ADD
# ============================================================


class Solution:

    def romanToInt(self, s: str) -> int:

        # Store the value of every Roman symbol
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # This will store our final answer
        total = 0

        # Go through every character of the Roman numeral
        for i in range(len(s)):

            # Check two things:
            #
            # 1. Is there a next character?
            # 2. Is the current value smaller than the next value?
            #
            # Example:
            # IV
            #
            # I = 1
            # V = 5
            #
            # 1 < 5 → subtract I

            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:

                # Current value is smaller,
                # so subtract it
                total -= roman[s[i]]

            else:

                # Otherwise, add the current value
                total += roman[s[i]]

        # Return the final integer
        return total


# ============================================================
# TESTING
# ============================================================

solution = Solution()

print(solution.romanToInt("III"))      # 3
print(solution.romanToInt("LVIII"))    # 58
print(solution.romanToInt("MCMXCIV"))  # 1994
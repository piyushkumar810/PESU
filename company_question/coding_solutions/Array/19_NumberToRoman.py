class Solution:

    def intToRoman(self, num: int) -> str:

        # Roman values arranged from largest to smallest
        # Special combinations like 900, 400, 90, 40,
        # 9 and 4 are also included.
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        # Corresponding Roman symbols
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        # Store the final Roman numeral
        result = ""

        # Go through every Roman value
        for i in range(len(values)):

            # Keep using this symbol while its value
            # can be subtracted from num
            while num >= values[i]:

                # Add the corresponding Roman symbol
                result += symbols[i]

                # Reduce num
                num -= values[i]

        return result


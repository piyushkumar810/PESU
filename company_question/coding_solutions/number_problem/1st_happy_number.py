# Problem Statement
'''
A number is called a happy number if:
--Replace the number with the sum of the squares of its digits.
--Repeat the process.
--If the number eventually becomes 1, it is a happy number.
--If the process enters a cycle that does not include 1, it is not a happy number.
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return n == 1

happy=Solution()
n=int(input("enter a number: "))
print(happy.isHappy(n))
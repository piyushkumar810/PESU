
class Solution:
    def climbStairs(self, n: int) -> int:

        # If n is 1 or 2, directly return n
        if n <= 2:
            return n

        # Initialize first two values
        a = 1
        b = 2

        # Calculate ways for remaining steps
        for i in range(3, n + 1):

            # Add previous two values
            current = a + b

            # Move values forward
            a = b
            b = current

        return b


# Input
n = 5

# Create Solution object
solution = Solution()

# Call the function
result = solution.climbStairs(n)

# Print output
print("Number of steps:", n)
print("Total ways to climb:", result)

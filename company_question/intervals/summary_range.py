
"""
LeetCode 228: Summary Ranges

Given a sorted array of unique integers, summarize
consecutive numbers into ranges.

Example:
Input:  [0, 1, 2, 4, 5, 7]
Output: ["0->2", "4->5", "7"]

Approach:
1. Start a range at the current number.
2. Continue while the next number is consecutive.
3. If the range has multiple numbers, use "start->end".
4. Otherwise, store the number alone.
"""

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]

            # Extend the range while numbers are consecutive
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1

            end = nums[i]

            # Format the range
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))

            # Move to the next number
            i += 1

        return result


# Example
nums = [0, 1, 2, 4, 5, 7]
solution = Solution()

print(solution.summaryRanges(nums))

# Output: ['0->2', '4->5', '7']

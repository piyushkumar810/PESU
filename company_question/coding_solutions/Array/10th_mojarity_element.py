# Question: Majority Element

'''
Given an integer array `nums` of size `n`, return the majority element.
The majority element is the element that appears more than `⌊n/2⌋` times.
You may assume that the majority element always exists in the array.

Example 1:
Input:
nums = [3,2,3]

Output:
3

Explanation:
Array size = 3
⌊3/2⌋ = 1
Element 3 appears 2 times, which is greater than 1.
Therefore, 3 is the majority element.

Example 2:
Input:
nums = [2,2,1,1,1,2,2]

Output:
2

Explanation:
Array size = 7
⌊7/2⌋ = 3
Element 2 appears 4 times, which is greater than 3.
Therefore, 2 is the majority element.
'''
def majority_element(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    n = len(nums)

    for key, value in freq.items():
        if value > n // 2:
            return key


nums = [2,2,1,1,1,2,2]

print(majority_element(nums))




# For full marks (5/5), use Boyer-Moore Voting Algorithm:
def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

# Time Complexity: O(n)
# Space Complexity: O(1)
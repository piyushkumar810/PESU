'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''


# ------------------------- stratagy
'''
for 0 stairs - 0 way
for 1 stairs - 1 way(1)
for 2 stairs - 2 way(1+1, 2)
for 3 stairs - 3 ways(1+1+1, 2+1, 1+2)
for 4 stairs - 5 ways(1+1+1+1, 2+2, 1+1+2, 2+1+1, 1+2+1)
for 5 stairs - 8 ways

this is nothing but a fibnaccio series

'''

# class Solution(object):
#     def climbStairs(self, n):
#         # print("total no of staires are ",n)

#         if n<=2:
#             return n
        
#         prev1=2
#         prev2=1
#         for i in range(3,n+1):
#             curr=prev1+prev2
#             prev2=prev1
#             prev1=curr

#         return prev1
        

# obj1=Solution()
# n1=int(input("enter total how many staires are there :"))
# print(obj1.climbStairs(n1))
        

class Solution:
    def staires(self,n):
        if n<=2:
            return n
        
        prev1=1
        prev2=2
        for i in range(3,n+1):
            curr=prev2+prev1
            prev1=prev2
            prev2=curr
        
        return prev2
    
obj2=Solution()
print(obj2.staires(5))
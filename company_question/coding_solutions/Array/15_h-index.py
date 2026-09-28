'''You are given an integer array citations, where citations[i] represents the number of citations received by a researcher's ith paper.

The h-index is the maximum value of h such that the researcher has published at least h papers, and each of those papers has been cited at least h times.

Example 1
Input:  citations = [3,0,6,1,5]
Output: 3

Explanation:

The researcher has 5 papers with:

[3, 0, 6, 1, 5]

There are 3 papers with at least 3 citations:

3  → 3 citations
6  → 6 citations
5  → 5 citations

So:

h = 3

There are not 4 papers with at least 4 citations, so the answer is:

3'''

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)

        h = 0

        for i in range(len(citations)):

            if citations[i] >= i + 1:
                h = i + 1
            else:
                break

        return h


# Test
citations = [3, 0, 6, 1, 5]

obj = Solution()

print(obj.hIndex(citations))
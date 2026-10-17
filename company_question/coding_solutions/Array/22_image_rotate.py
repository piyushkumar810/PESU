
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        LeetCode 48: Rotate Image

        Question:
        You are given an n x n 2D matrix representing an image.
        Rotate the image by 90 degrees clockwise.

        Modify the matrix in-place.
        Do not create another 2D matrix.
        Do not return anything.

        Example:
        Input:
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        Output:
        [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

        Approach:
        1. Transpose the matrix.
        2. Reverse each row.
        """

        n = len(matrix)

        # Step 1: Transpose the matrix
        # Swap matrix[i][j] with matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()


# Test the code
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Solution().rotate(matrix)

for row in matrix:
    print(row)

# Output:
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]

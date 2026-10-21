from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Question:
        Given an m x n integer matrix, if an element is 0,
        set its entire row and column to 0.

        You must modify the matrix in-place.

        Example 1:
        Input:
        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

        Output:
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]

        Example 2:
        Input:
        matrix = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]

        Output:
        [
            [0, 0, 0, 0],
            [0, 4, 5, 0],
            [0, 3, 1, 0]
        ]

        Approach:
        1. Find all rows and columns containing zero.
        2. Store their indices in sets.
        3. Set those rows and columns to zero.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0
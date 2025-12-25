"""
Matrix Template
===============

Complexity Summary
------------------
| Operation | Time     | Space | Notes |
|-----------|----------|-------|-------|
| Traversal | O(M*N)   | O(1)  | Nested loops |
| Transpose | O(M*N)   | O(1)  | Swap (i, j) with (j, i) |
| Rotate    | O(M*N)   | O(1)  | In-place rotation |

Best Practices:
- **Directions**: Use `dirs = [(0,1), (0,-1), (1,0), (-1,0)]` for neighbors.
- **Boundaries**: Always check `0 <= r < R` and `0 <= c < C`.
- **In-place**: Many matrix problems ask for O(1) space modification.
"""

from typing import List

class MatrixTemplate:
    """
    Encapsulates high-level generic template for Matrix operations.
    """

    def traverse(self, matrix: List[List[int]]):
        """
        Standard Traversal.
        """
        if not matrix: return
        R, C = len(matrix), len(matrix[0])
        
        for r in range(R):
            for c in range(C):
                val = matrix[r][c]
                # Process val

    def get_neighbors(self, matrix: List[List[int]], r: int, c: int):
        """
        Get valid 4-directional neighbors.
        """
        R, C = len(matrix), len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                neighbors.append((nr, nc))
        return neighbors


class MatrixExamples:
    """
    Concrete examples of Matrix patterns.
    """

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Concrete Example: Rotate Image (LeetCode 48).
        Rotate n x n matrix 90 degrees clockwise in-place.
        
        Strategy: Transpose -> Reverse Rows.
        """
        n = len(matrix)
        
        # 1. Transpose (Swap i,j with j,i)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # 2. Reverse each row
        for i in range(n):
            matrix[i].reverse()

    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Concrete Example: Spiral Matrix (LeetCode 54).
        """
        result = []
        if not matrix: return result
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Left -> Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # Top -> Bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # Right -> Left
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # Bottom -> Top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
                
        return result

if __name__ == "__main__":
    # 2. Examples
    examples = MatrixExamples()
    
    # Rotate
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    examples.rotate(mat)
    print(f"Example Result (Rotate): {mat}") # [[7,4,1],[8,5,2],[9,6,3]]
    
    # Spiral
    mat2 = [[1,2,3],[4,5,6],[7,8,9]]
    res_spiral = examples.spiral_order(mat2)
    print(f"Example Result (Spiral): {res_spiral}") # [1,2,3,6,9,8,7,4,5]

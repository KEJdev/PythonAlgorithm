class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
                
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False]*cols for _ in range(rows)]
        answer = []

        row = 0
        col = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]  # → ↓ ← ↑

        idx = 0

        while len(answer) != len(matrix)* len(matrix[0]):
            answer.append(matrix[row][col])
            visited[row][col] = True

            next_row = row + directions[idx][0] # →
            next_col = col + directions[idx][1] # ↓

            if (0 <= next_row < rows and
                0 <= next_col < cols and
                not visited[next_row][next_col]):
                row , col = next_row , next_col
            else:
                idx = (idx + 1)%4
                row += directions[idx][0]
                col += directions[idx][1]
        return answer 
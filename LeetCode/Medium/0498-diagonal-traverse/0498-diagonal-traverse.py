class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        diagonals = [[] for _ in range(m + n - 1)]

        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])

        result = []
        for index, group in enumerate(diagonals):
            if index % 2 == 0:
                result.extend(group[::-1])  # 슬라이싱으로 뒤집기
            else:
                result.extend(group)

        return result

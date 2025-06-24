class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        answer = [[]]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                k = i+j 
                if len(answer) != k:
                    answer.append([])     
                answer[k].append(mat[i][j])
        
        mat = []
        for index, sublist in enumerate(answer) :
            if index%2 == 0:
                mat.extend(list(reversed(sublist)))
            else:
                mat.extend(sublist)
        
        return mat
        
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        elif numRows ==2:
            return [[1],[1,1]]
        
        answer = [[1]]
        temp = []
        
        for row in range(1, numRows+1):
            for col in range(row-1):
                if col == 0:
                    temp.append(answer[row-1][col])
                else:
                    num = answer[row-1][col] + answer[row-1][col-1]
                    temp.append(num)

            temp.append(1)
            answer.append(temp)
            temp = []
        return answer[1:] 




        
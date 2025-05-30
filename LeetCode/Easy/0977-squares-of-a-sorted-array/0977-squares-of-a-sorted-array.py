class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        answer = []
        for x in nums:
            answer.append(x**2)
        
        answer.sort()
        return answer
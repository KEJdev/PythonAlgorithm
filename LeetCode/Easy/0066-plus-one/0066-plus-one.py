class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        answer = ''
        for num in digits:
            answer += str(num)
        
        answer = list(str(int(answer)+1))
        return list(map(int, answer))
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums_list = [x for x in range(1, len(nums)+1)]
        set_nums = set(nums)
        answer = []
        
        for value in nums_list:
            if value not in set_nums:
                answer.append(value)
        
        return answer
        
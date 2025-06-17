class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        max_value = max(nums)
        max_index = nums.index(max_value)
        temp_list = []
        
        for value in nums:
            if max_value < value*2 and max_index != nums.index(value):
                return -1

        return max_index 

        
        
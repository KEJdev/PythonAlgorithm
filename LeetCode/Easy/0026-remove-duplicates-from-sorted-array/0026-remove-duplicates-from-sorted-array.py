class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = set(nums)
        nums[0:0] += sorted(list(set(nums)))
        
        
        return len(k)
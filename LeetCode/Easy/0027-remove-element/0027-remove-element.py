class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = 0
        
        for idx, item in enumerate(nums):
            
            # 만약에 val 값과 nums 값이 일치 하지 않으면
            if item != val:
                answer += 1
                
            # 일치한다면 
            else:
                nums[idx] = -1
        nums.sort(reverse=True)

        return answer
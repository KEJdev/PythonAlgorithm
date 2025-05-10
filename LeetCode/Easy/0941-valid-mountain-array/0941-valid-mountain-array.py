class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) <=2:
            return False
        
        check = []
        for idx in range(len(arr)-1):

            # 상승
            if arr[idx] < arr[idx+1]:
                check.append(1)
                if 0 in check:
                    return False

            # 하강
            elif arr[idx] > arr[idx+1]:
                check.append(0)
                if 1 not in check:
                    return False

            if idx+1 == len(arr)-1:
                if arr[-1] < arr[-2]:
                    check.append(0)
                else:
                    return False

            if arr[idx] == arr[idx+1]:
                return False

        if check[-1] != 0:
            return False
        
        return True
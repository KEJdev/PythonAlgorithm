class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        result = []

        for i in range(len(arr)):
            if 2 * arr[i] in arr:
                result.append(arr.index(2 * arr[i]) != i)
            else:
                result.append(False)
        return max(result)

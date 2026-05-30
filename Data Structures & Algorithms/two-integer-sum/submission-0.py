class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i, j=0, 1
        summ = 0 

        for i in range(len(nums)-1):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i]+nums[j] == target:
                    return [i,j]
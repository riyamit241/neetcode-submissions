class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        unique = list(set(nums))
        unique.sort()
        count, maxx = 1, 1

        for i in range(len(unique)-1):
            if unique[i+1] == unique[i]+1:
                count += 1
            else:
                count = 1
            maxx = max(count, maxx)
        
        return maxx
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        unique = set(nums)
        longest = 1

        for num in unique:
            if num-1 not in unique: # only start if curr is start of seq
                curr = num
                streak = 1 

                while curr+1 in unique:
                    streak +=1
                    curr +=1

                    longest = max(longest, streak)
        return longest
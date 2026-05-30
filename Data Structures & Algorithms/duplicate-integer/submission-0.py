class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt = {}

        for num in nums:
            if num in dictt:
                return True
            else: 
                dictt[num]=1
        return False
            
        
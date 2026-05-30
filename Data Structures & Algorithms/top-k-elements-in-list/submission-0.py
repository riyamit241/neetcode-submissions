class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {} # to keep track of elements

        for num in nums:
            if num in output:
                output[num] += 1
            else:
                output[num] = 1

        sorted_nums = sorted(output, key=output.get, reverse=True)

        return sorted_nums[:k]
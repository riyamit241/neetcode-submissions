class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, 0

        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    if i == j:
                        continue
                    return [i+1, j+1]


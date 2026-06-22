class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        indexes = []

        while l < r:
            if numbers[l] + numbers[r] == target:
                indexes.append(l + 1)
                indexes.append(r + 1)
                return indexes
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
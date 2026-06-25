class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        amt = (j - i) * min(heights[i], heights[j])

        while i < j:
            left = heights[i]
            right = heights[j]
            curr = (j - i) * min(left, right)

            if curr > amt:
                amt = curr

            if left < right:
                i += 1
            else:
                j -= 1
        
        return amt
            
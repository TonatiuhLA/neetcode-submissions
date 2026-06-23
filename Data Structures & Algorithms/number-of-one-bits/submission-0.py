class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0

        for i in range(0, 33):
            a = n & 1
            if a == 1:
                num += 1
            n >>= 1
        
        return num
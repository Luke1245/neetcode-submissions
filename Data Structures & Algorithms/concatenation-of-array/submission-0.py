class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ansArray = [0] * (n * 2)

        for i in range(n * 2):
            ansArray[i] = nums[i % n]
        
        return ansArray
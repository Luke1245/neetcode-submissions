class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ansArray = [0] * (n * 2)

        for i in range(n):
            ansArray[i] = nums[i]
            ansArray[i + n] = nums[i]  

        return ansArray
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0 ,0] 

        for colour in nums:
            counts[colour] += 1

        index = 0
        for i in range(len(counts)):
            for _ in range(counts[i]):
                nums[index] = i
                index += 1
        
        return nums 

        

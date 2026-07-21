class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            greatest_right = 0
            for j in range(i + 1, len(arr)):
                greatest_right = max(greatest_right, arr[j])
            
            arr[i] = greatest_right
        
        arr[-1] = -1
        return arr
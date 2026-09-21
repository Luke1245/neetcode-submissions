# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        mid = len(pairs) // 2

        arr1 = self.mergeSort(pairs[:mid])
        arr2 = self.mergeSort(pairs[mid:])

        arr = self.merge(arr1, arr2)

        return arr

    def merge(self, arr1: List[Pair], arr2: List[Pair]) -> List[Pair]:
        i = j = 0
        arr = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i].key <= arr2[j].key:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1
            
        return arr + arr1[i:] + arr2[j:]



class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num = len(students)
        count = Counter(students)

        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
                num -= 1
            else:
                return num
        
        return num
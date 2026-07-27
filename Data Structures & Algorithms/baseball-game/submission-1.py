class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # use a stack
        scores = []

        for i in range(len(operations)):
            try:
                value = int(operations[i])
                scores.append(value)
            except:
                if operations[i] == "+":
                    firstVal = scores.pop()
                    secondVal = scores.pop()

                    scores.append(secondVal)
                    scores.append(firstVal)
                    scores.append(firstVal + secondVal)
                elif operations[i] == "D":
                    scores.append(scores[-1] * 2)
                else:
                    scores.pop()
        
        return sum(scores)
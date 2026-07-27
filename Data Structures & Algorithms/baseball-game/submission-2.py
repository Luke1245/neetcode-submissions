class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # use a stack
        scores = []
        total = 0

        for i in range(len(operations)):
            try:
                value = int(operations[i])
                scores.append(value)
                total += value
            except:
                if operations[i] == "+":
                    firstVal = scores.pop()
                    secondVal = scores.pop()
                    total += (firstVal + secondVal)

                    scores.append(secondVal)
                    scores.append(firstVal)
                    scores.append(firstVal + secondVal)
                elif operations[i] == "D":
                    total += (scores[-1] * 2)
                    scores.append(scores[-1] * 2)
                else:
                    value = scores.pop()
                    total -= value
        
        return total
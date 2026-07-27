class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        parenMaps = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:
            if ch in parenMaps:
                if openStack and openStack[-1] == parenMaps[ch]:
                    openStack.pop()
                else:
                    return False
            else:
                openStack.append(ch)
        
        return True if not openStack else False
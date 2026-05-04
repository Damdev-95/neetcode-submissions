class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in mapping.values():  # opening bracket
                stack.append(c)
            else:  # closing bracket
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()

        return len(stack) == 0
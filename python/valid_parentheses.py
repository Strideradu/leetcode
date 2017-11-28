class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for symbol in s:
            if symbol in ['(', '{', '[']:
                stack.append(symbol)

            if symbol == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False

            if symbol == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False

            if symbol == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False

        if len(stack) > 0:
            return False
        else:
            return True

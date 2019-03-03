class Solution:
    def isValid(self, S: str) -> bool:
        stack=[]
        for char in S:
            if char == 'c':
                if len(stack)<2 or stack[-2]!='a' or stack[-1]!='b':
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(char)
            
        return len(stack)==0
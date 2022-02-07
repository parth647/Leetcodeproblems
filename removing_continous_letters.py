class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for it in s:
            if(not stack):
                stack.append(it)
            elif(stack[-1]==it):
                stack.pop()
            else:
                stack.append(it)
            
        return "".join(stack)
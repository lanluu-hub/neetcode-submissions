class Solution:
    def isValid(self, s: str) -> bool:
        # stack: (
        # curr_s: (
        # if [i-1] == '(' [i] == ')' .pop()
        # at the end of loop, if stack empty return true, else false
        stack = []
        for c in s: 
            if not stack: 
                stack.append(c)
            else:
                print(c)
                match c:
                    case ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    case '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
                    case ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False
                    case _:
                        stack.append(c)

        if stack == []:
            return True
        return False  


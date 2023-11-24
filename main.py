def isValid(self, s: str) -> bool:
    stack = []
    closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

    for c in s:  # c is character
        if c in closeToOpen:
            # if stack is not null AND the last item in stack is in closeToOpen
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False

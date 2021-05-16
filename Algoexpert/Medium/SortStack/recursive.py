def sortStack(stack):
    if len(stack) == 0:
        return stack
    top = stack.pop()
    sortStack(stack)
    insert(stack,top)
    return stack
def insert(stack,value):
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return
    top = stack.pop()
    insert(stack,value)
    stack.append(top)
operations = ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
output = []

stack = []
min_stack = []

for op in operations:
    if op == "MinStack":
        stack = []
        min_stack = []
        output.append(None)
    elif op == "push":
        continue  
    elif isinstance(op, int):
        val = op
        stack.append(val)
        if not min_stack or val <= min_stack[-1]:
            min_stack.append(val)
        output.append(None)
    elif op == "pop":
        if stack:
            if stack[-1] == min_stack[-1]:
                min_stack.pop()
            stack.pop()
        output.append(None)
    elif op == "top":
        output.append(stack[-1] if stack else None)
    elif op == "getMin":
        output.append(min_stack[-1] if min_stack else None)

print(output)

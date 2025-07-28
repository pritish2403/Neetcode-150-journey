s = "[]"

stack = []
mapping = {')': '(', '}': '{', ']': '['}

is_valid = True
for char in s:
    if char in mapping.values():
        stack.append(char)
    elif char in mapping:
        if not stack or stack[-1] != mapping[char]:
            is_valid = False
            break
        stack.pop()
    else:
        is_valid = False
        break

if stack:
    is_valid = False

print(is_valid)

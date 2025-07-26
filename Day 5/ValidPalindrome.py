s = "Was it a car or a cat I saw?"

cleaned = ''
for c in s:
    if c.isalnum():
        cleaned += c.lower()

is_palindrome = cleaned == cleaned[::-1]
print(is_palindrome)

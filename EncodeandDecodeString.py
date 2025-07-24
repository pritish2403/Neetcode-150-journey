strs = ["neet", "code", "love", "you"]
encoded = ""
for s in strs:
    encoded += str(len(s)) + "#" + s

s = encoded
decoded = []
i = 0

while i < len(s):
    j = i
    while s[j] != '#':
        j += 1

    length = int(s[i:j])
    i = j + 1
    j = i + length
    decoded.append(s[i:j])
    i = j

print(decoded)

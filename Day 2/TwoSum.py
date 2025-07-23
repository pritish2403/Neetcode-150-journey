a = [4,5,6]
target = 10

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == target:
            print(f'[{i}, {j}]')
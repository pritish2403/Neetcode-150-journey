numbers = [1, 2, 3, 4]
target = 3

left, right = 0, len(numbers) - 1

while left < right:
    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        print([left + 1, right + 1])
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

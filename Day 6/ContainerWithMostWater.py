heights = [1, 7, 2, 5, 4, 7, 3, 6]
left, right = 0, len(heights) - 1
max_area = 0

while left < right:
    height = min(heights[left], heights[right])
    width = right - left
    area = height * width
    max_area = max(max_area, area)

    if heights[left] < heights[right]:
        left += 1
    else:
        right -= 1

print(max_area)

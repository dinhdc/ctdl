def max_area(height) -> int:
    left = res = 0
    right = len(height) - 1
    while right > left:
        width = right - left
        h = min(height[left], height[right])
        size = width * h
        res = size if size > res else res
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return res

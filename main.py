def can_nest(box1, box2):
    return all(x < y for x, y in zip(box1, box2))

def longest_box_sequence(boxes):
    # Sort the boxes based on dimensions
    boxes.sort(key=lambda box: (box[0], box[1], box[2]))

    n = len(boxes)
    dp = [1] * n  # dp[i] will store the maximum number of boxes ending with box i

    for i in range(n):
        for j in range(i):
            if can_nest(boxes[j], boxes[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# boxes = [(1, 5, 6), (3, 4, 5), (1, 2, 3), (6, 2, 8), (5, 5, 1), (2, 3, 1)]
# boxes = [(1, 1, 1), (2, 2, 2)]
# boxes = [(5, 4, 6), (6, 7, 8), (3, 2, 1), (4, 5, 6), (6, 5, 7)]
print(longest_box_sequence(boxes))

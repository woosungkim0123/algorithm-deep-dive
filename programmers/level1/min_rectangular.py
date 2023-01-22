def solution(sizes):

    return max(max(size) for size in sizes) * max(min(size) for size in sizes)


solution([[60, 50], [30, 70], [60, 30], [80, 40]])

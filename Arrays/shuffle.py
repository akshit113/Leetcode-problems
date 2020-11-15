def shuffle(self, nums: List[int], n: int) -> List[int]:
    x = nums[0:n]
    y = nums[n:]
    l = []
    for i in range(n):
        l.append(x[i])
        l.append(y[i])
    return l
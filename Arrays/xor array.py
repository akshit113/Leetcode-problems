def xorOperation(n, start):
    nums = [start + 2 * i for i in range(n)]
    xor = 0
    idx = 0
    while idx <= len(nums) - 1:
        xor = xor ^ nums[idx]
        idx += 1
    return xor


if __name__ == '__main__':
    n = 5
    start = 0
    xorOperation(n, start)

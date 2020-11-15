def twoSum(nums, target):
    dc = dict()

    for idx, val in enumerate(nums):
        comp = target - val
        if comp not in dc.keys():
            dc[val] = idx
        else:
            print('test')
            idx2 = dc[comp]
            break
    [a, b] = sorted([idx, idx2])
    return a,b


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    a, b = twoSum(nums, target)

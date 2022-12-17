def solve(nums, target):
    for i in range(len(nums)):
        a = nums[i]
        for j in range(len(nums)):
            b = nums[j]
            if i != j and a + b == target:
                return [i, j]


def twoSum(nums, target):
    t2 = int(target/2)
    if target%2 !=0:
        t2 -= 0.5
    for n in range(0, t2+1):
        if n in nums:
            return [nums.index(n), nums.index(target-n)]

twoSum([3,2,4], 6)
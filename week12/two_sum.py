
def two_sum(nums, target):
    for i in nums:
        for j in range(1, len(nums)):
            if i + nums[j] == target:
                return [nums.index(i), j]

def main():
    nums = [2, 5, 5, 12]
    target = 14
    print(two_sum(nums, target))

if __name__ == '__main__':
    main()
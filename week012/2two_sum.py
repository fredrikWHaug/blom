
def two_sum(nums, target):
    index = 0
    for i in nums:
        index += 1
        for j in range(index, len(nums)):
            if i + nums[j] == target:
                return [nums.index(i), j]
            
def main():
    nums = [0, 0, 0, 2, 3]
    target = 5
    print(two_sum(nums, target))

if __name__ == '__main__':
    main()

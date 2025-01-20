def find_missing_num(nums):
    n = len(nums) + 1
    total = n * (n+1) // 2 # sum of the first n numbs
    current_sum = sum(nums)
    return total - current_sum

nums = [1,2,3,4,6,7,8]
print(find_missing_num(nums))
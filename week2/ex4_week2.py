#Write code that uses slicing to get rid of the the second 8 so that here are only two 8’s in the list bound to the variable nums.

nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]
nums = nums[0:4] + nums[5:(len(nums))]
print(nums)
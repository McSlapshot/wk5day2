#Find Single Number
#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#Example 1:
#Input: nums = [2,2,1]
#Output: 1
#Example 2:
#nput: nums = [4,1,2,1,2]					
#utput: 4
#Example 3:
#Input: nums = [1]
#Output: 1
def Find_Single(list_1):
    for num in list_1:
        if list_1.count(num) == 1:
            return num


print(Find_Single([4,1,2,1,2]))
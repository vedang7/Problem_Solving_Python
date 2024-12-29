'''
1752. Check if Array Is Sorted and Rotated
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
'''

from collections import deque
def is_sorted(lst):
    return lst == sorted(lst)

def check(nums: list = None) -> bool:
        left = 0
        right = left + 1
        is_list_sorted = is_sorted(nums)
        if nums[len(nums) - 1] < nums[0]:
                while right < len(nums):
                        if nums[left] <= nums[right]:
                                left += 1
                                right += 1
                        else:
                                left = right
                                right = right + 1 if right < len(nums) - 1 else -1
                                if right == -1:
                                        if nums[left] > nums[0]:
                                                return False
                                        else:
                                                return True
                
                return True
        else:
                if is_list_sorted:
                        return True
                return False
        
        # Second solution 
        
        # high=len(nums)
        # count=0
        # for i in range(high):
        #     if(nums[i] > nums[(i+1)% high]):
        #         count+=1
        #     if(count > 1):
        #         return False
        # return True
                     

print("hello" if check([2,1,3,4]) else "bye")
print("hello" if check([3, 4, 5, 1, 2]) else "bye")
# import ipdb; ipdb.set_trace()
print("hello" if check([1, 2, 3,]) else "bye")

# [3, 4, 5, 1, 2]

# [2, 1, 3, 4]